r"""
Examples of finite dimensional algebras with basis
"""
#*****************************************************************************
#  Copyright (C) 2008-2009 Franco Saliola <saliola@gmail.com>
#
#  Distributed under the terms of the GNU General Public License (GPL)
#                  http://www.gnu.org/licenses/
#*****************************************************************************

from sage.misc.cachefunc import cached_method
from sage.categories.all import FiniteDimensionalAlgebrasWithBasis
from sage.combinat.free_module import CombinatorialFreeModule

class KroneckerQuiverPathAlgebra(CombinatorialFreeModule):
    r"""
    An example of a finite dimensional algebra with basis: the path algebra of
    the Kronecker quiver.

    This class illustrates a minimal implementation of a finite dimensional
    algebra with basis.
    """

    def __init__(self, R):
        r"""
        EXAMPLES::

            sage: A = FiniteDimensionalAlgebrasWithBasis(QQ).example(); A
            An example of a finite dimensional algebra with basis: the path algebra of the Kronecker quiver (containing the arrows a:x->y and b:x->y) over Rational Field 
            sage: TestSuite(A).run()

        """
        basis_keys = ['x', 'y', 'a', 'b']
        self._nonzero_products = {
            'xx':'x', 'xa':'a', 'xb':'b',
            'yy':'y', 'ay':'a', 'by':'b'
            }

        CombinatorialFreeModule.__init__(self, R, basis_keys, category = FiniteDimensionalAlgebrasWithBasis(R))

    def _repr_(self):
        r"""
        EXAMPLES::

            sage: FiniteDimensionalAlgebrasWithBasis(QQ).example() # indirect doctest
            An example of a finite dimensional algebra with basis: the path algebra of the Kronecker quiver (containing the arrows a:x->y and b:x->y) over Rational Field 
        """
        return "An example of a finite dimensional algebra with basis: the path algebra of the Kronecker quiver (containing the arrows a:x->y and b:x->y) over %s "%(self.base_ring())

    def one(self):
        r"""
        Returns the multiplicative identity element of the algebra, as per :meth:`AlgebrasWithBasis.ParentMethods.one_basis`.

        EXAMPLES::

            sage: A = FiniteDimensionalAlgebrasWithBasis(QQ).example()
            sage: A.one()
            x + y
        """
        return self.sum_of_monomials(['x', 'y'])

    def product_on_basis(self, w1, w2):
        r"""
        Product of basis elements, as per :meth:`AlgebrasWithBasis.ParentMethods.product_on_basis`.

        EXAMPLES::

            sage: A = FiniteDimensionalAlgebrasWithBasis(QQ).example()

        Here is the multiplication table for the algebra::

            sage: matrix([[p*q for q in A.basis()] for p in A.basis()])
            [x 0 a b]
            [0 y 0 0]
            [0 a 0 0]
            [0 b 0 0]

        Here we take some products of linear combinations of basis elements::

            sage: x, y, a, b = A.basis()
            sage: a * (1-b)^2 * x
            0
            sage: x*a + b*y
            a + b
            sage: x*x
            x
            sage: x*y
            0
            sage: x*a*y
            a
        """
        if w1+w2 in self._nonzero_products:
            return self.monomial(self._nonzero_products[w1+w2])
        else:
            return self.zero()

    @cached_method
    def algebra_generators(self):
        r"""
        Returns the generators of this algebra, as per :meth:`Algebras.ParentMethods.algebra_generators`.

        EXAMPLES::

            sage: A = FiniteDimensionalAlgebrasWithBasis(QQ).example(); A
            An example of a finite dimensional algebra with basis: the path algebra of the Kronecker quiver (containing the arrows a:x->y and b:x->y) over Rational Field
            sage: A.algebra_generators()
            Finite family {'y': y, 'x': x, 'b': b, 'a': a}
        """
        return self.basis()

    def _repr_term(self, p):
        r"""
        This method customizes the string representation of the basis element indexed by ``p``.

        In this example, we just return the string representation of ``p`` itself.

        EXAMPLES::

            sage: A = FiniteDimensionalAlgebrasWithBasis(QQ).example()
            sage: A.one()
            x + y
        """
        return str(p)

Example = KroneckerQuiverPathAlgebra

