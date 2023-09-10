import networkx as nx
from typing import List
from funciones2 import calculo_distancia_euclidiana

class Node(object):
    def __init__(self):
        self.padre = None
        self.izquierda = None
        self.derecha = None
        self.feature = None
        self.split = None

    def __str__(self):
        return "feature: %s, split: %s" % (str(self.feature), str(self.split))

    @property
    def brother(self): # busqueda de nodo hermanos
        if not self.padre:
            ret = None
        else:
            if self.padre.izquierda is self:
                ret = self.padre.derecha
            else:
                ret = self.padre.izquierda
        return ret


class KDTree(object):
    def __init__(self):
        """KD Tree class to improve search efficiency in KNN.

        Attributes:
            root: the root node of KDTree.
        """
        self.root = Node()

    def __str__(self):
        """Show the relationship of each node in the KD Tree.
        Returns:
            str -- KDTree Nodes information.
        """
        ret = []
        i = 0
        cola = [(self.root, -1)]
        while cola:
            nd, idx_padre = cola.pop(0)
            ret.append("%d -> %d: %s" % (idx_padre, i, str(nd)))
            if nd.izquierda:
                cola.append((nd.izquierda, i))
            if nd.derecha:
                cola.append((nd.derecha, i))
            i += 1
        return "\n".join(ret)

    def _get_median_idx(self, X, idxs, feature):
        """Calculate the median of a column of data.

        Arguments:
            X {list} -- 2d list object with int or float.
            idxs {list} -- 1D list with int.
            feature {int} -- Feature number.
            sorted_idxs_2d {list} -- 2D list with int.

        Returns:
            list -- The row index corresponding to the median of this column.
        """

        n = len(idxs)
        # Ignoring the number of column elements is odd and even.
        k = n // 2
        # Get all the indexes and elements of column j as tuples.
        col = map(lambda i: (i, X[i][feature]), idxs)
        # Sort the tuples by the elements' values
        # and get the corresponding indexes.
        sorted_idxs = map(lambda x: x[0], sorted(col, key=lambda x: x[1]))
        # Search the median value.
        median_idx = list(sorted_idxs)[k]
        return median_idx

    def _get_variance(self, X, idxs, feature): ### usada
        """Calculate the variance of a column of data.

        Arguments:
            X {list} -- 2d list object with int or float.
            idxs {list} -- 1D list with int.
            feature {int} -- Feature number.

        Returns:
            float -- variance
        """

        n = len(idxs)
        col_sum = col_sum_sqr = 0
        for idx in idxs:
            xi = X[idx][feature]
            col_sum += xi
            col_sum_sqr += xi ** 2
        # D(X) = E{[X-E(X)]^2} = E(X^2)-[E(X)]^2
        return col_sum_sqr / n - (col_sum / n) ** 2

    def _choose_feature(self, X, idxs):
        """Choose the feature which has maximum variance.

        Arguments:
            X {list} -- 2d list object with int or float.
            idxs {list} -- 1D list with int.

        Returns:
            feature number {int}
        """

        m = len(X[0])-1 # paráque no revise columna 5
        variances = map(lambda j: (j, self._get_variance(X, idxs, j)), range(m))
        return max(variances, key=lambda x: x[1])[0]

    def _split_feature(self, X, idxs, feature, median_idx):
        """Split indexes into two arrays according to split point.

        Arguments:
            X {list} -- 2d list object with int or float.
            idx {list} -- Indexes, 1d list object with int.
            feature {int} -- Feature number.
            median_idx {float} -- Median index of the feature.

        Returns:
            list -- [izquierda idx, derecha idx]
        """

        idxs_split = [[], []]
        split_val = X[median_idx][feature]
        for idx in idxs:
            # Keep the split point in current node.
            if idx == median_idx:
                continue
            # Split
            xi = X[idx][feature]
            if xi < split_val:
                idxs_split[0].append(idx)
            else:
                idxs_split[1].append(idx)
        return idxs_split

    def construir_kdtree(self, X, discriminante):
        # Initialize with node, indexes
        nd = self.root
        idxs = range(len(X)) # de 0 a numero de puntos (10)
        cola = [(nd, idxs)]
        while cola:
            nd, idxs = cola.pop(0)
            n = len(idxs)
            # Stop split if there is only one element in this node
            if n == 1:
                nd.split = (X[idxs[0]], discriminante[idxs[0]])
                continue
            # Split
            feature = self._choose_feature(X, idxs)
            median_idx = self._get_median_idx(X, idxs, feature)
            idxs_izquierda, idxs_derecha = self._split_feature(X, idxs, feature, median_idx)
            # Update properties of current node
            nd.feature = feature
            nd.split = (X[median_idx], discriminante[median_idx])
            # Put children of current node in que
            if idxs_izquierda != []:
                nd.izquierda = Node()
                nd.izquierda.padre = nd
                cola.append((nd.izquierda, idxs_izquierda))
            if idxs_derecha != []:
                nd.derecha = Node()
                nd.derecha.padre = nd
                cola.append((nd.derecha, idxs_derecha))

    def _search(self, Xi, nd):
        """Search Xi from the KDTree until Xi is at an leafnode.

        Arguments:
            Xi {list} -- 1d list with int or float.

        Returns:
            node -- Leafnode.
        """

        while nd.izquierda or nd.derecha:
            if not nd.izquierda:
                nd = nd.derecha
            elif not nd.derecha:
                nd = nd.izquierda
            else:
                if Xi[nd.feature] < nd.split[0][nd.feature]:
                    nd = nd.izquierda
                else:
                    nd = nd.derecha
        return nd

    def _get_eu_dist(self, Xi, nd):
        """Calculate euclidean distance between Xi and node.

        Arguments:
            Xi {list} -- 1d list with int or float.
            nd {node}

        Returns:
            float -- Euclidean distance.
        """

        X0 = nd.split[0]
        return calculo_distancia_euclidiana(Xi, X0)

    def _get_hyper_plane_dist(self, Xi, nd):
        j = nd.feature
        X0 = nd.split[0]
        return abs(Xi[j] - X0[j])

    def busqueda_vecino_mas_cercano(self, Xi): # busqueda vecino mas cercano and backtracking
        # The leaf node after searching Xi.
        dist_best = float("inf")
        nd_best = self._search(Xi, self.root)
        cola = [(self.root, nd_best)]
        while cola:
            nd_root, nd_cur = cola.pop(0)
            dist = self._get_eu_dist(Xi, nd_root) # distancia entre punto y nodo
            # Update best node and distance.
            if dist < dist_best:
                dist_best, nd_best = dist, nd_root
            while nd_cur is not nd_root:
                # Distancia entre punto y nodo recorrido actual
                dist = self._get_eu_dist(Xi, nd_cur)
                # Update best node, distance and visit flag.
                if dist < dist_best:
                    dist_best, nd_best = dist, nd_cur
                # If it's necessary to visit brother node.
                if nd_cur.brother and dist_best > \
                        self._get_hyper_plane_dist(Xi, nd_cur.padre):
                    _nd_best = self._search(Xi, nd_cur.brother)
                    cola.append((nd_cur.brother, _nd_best))
                # Back track.
                nd_cur = nd_cur.padre
            punto_cercano=''    
        punto_cercano = str(nd_best)
        print(f'pto = {punto_cercano}')
        return nd_best
        #return punto_cercano[punto_cercano.index('['):punto_cercano.index(']')]
