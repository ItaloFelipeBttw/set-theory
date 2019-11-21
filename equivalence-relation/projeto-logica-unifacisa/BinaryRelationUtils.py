#coding: utf-8


class BinaryRelationUtils(object):
    """Class providing utilities to verify properties of a binary relation."""

    @staticmethod
    def verify_reflexivity(binary_relation, input_set):
        """
        This method verifies if a given binary relation is reflexive or not.

        Arguments:
        binary_relation - A subclass of the BinaryRelation class.

        input_set - A set closed under the binary relation.

        Return True if the binary relation in the given input set is reflexive
        or False if it is not.
        """
        rho = binary_relation.relation(input_set)
        for x in input_set:
            if (x, x) not in rho:
                return False

        return True
        pass

    @staticmethod
    def verify_symmetry(binary_relation, input_set):
        """
        This method verifies if a given binary relation is symmetric or not.

        Arguments:
        binary_relation - A subclass of the BinaryRelation class.

        input_set - A set closed under the binary relation.

        Return True if the binary relation in the given input set is symmetric
        or False if it is not.
        """
        rho = binary_relation.relation(input_set)
        for x in input_set:
            for y in input_set:
                if (x,y) in rho and (y,x) in rho:
                    return True
        return False
        pass
        
        

    @staticmethod
    def verify_transitivity(binary_relation, input_set):
        """
        This method verifies if a given binary relation is transitive or not.

        Arguments:
        binary_relation - A subclass of the BinaryRelation class.

        input_set - A set closed under the binary relation.

        Return True if the binary relation in the given input set is transitive
        or False if it is not.
        """
        rho = binary_relation.relation(input_set)

        for x in input_set:
            for y in input_set:
                for outro in input_set:
                    if (x, outro) in rho and (y, outro) in rho and (x, outro) not in rho:
                        return False
                    else:
                         return True

       
        pass

    @staticmethod
    def verify_antisymmetry(binary_relation, input_set):
        """
        This method verifies if a given binary relation is antisymmetric or not.

        Arguments:
        binary_relation - A subclass of the BinaryRelation class.

        input_set - A set closed under the binary relation.

        Return True if the binary relation in the given input set is 
        antisymmetric or False if it is not.
        """
        rho = binary_relation.relation(input_set)

        for x, y in rho:
            if (y, x) in rho and x != y:
                return False
            
        return True

        
        pass

        

    @staticmethod
    def verify_equivalency(binary_relation, input_set):
        """
        This method verifies if a given binary relation is an equivalence relation.

        Arguments:
        binary_relation - A subclass of the BinaryRelation class.

        input_set - A set closed under the binary relation.

        Return True if the binary relation in the given input set is 
        an equivalence relation or False if it is not.
        """
        return BinaryRelationUtils.verify_symmetry(binary_relation, input_set) and BinaryRelationUtils.verify_reflexivity(binary_relation, input_set) and BinaryRelationUtils.verify_transitivity(binary_relation, input_set)
        pass
    @staticmethod
    def get_partitioning(binary_relation, input_set):
        """
        This method first verifies if binary relation is an equivalence relation and, if it is, generates a partitioning of the input set using the binary relation. If the binary relation is not an equivalence relation, it returns None.

        Note: The partitioning of the set should be a list of subsets.

        Arguments:
        binary_relation - A subclass of the BinaryRelation class.

        input_set - A set closed under the binary relation.

        Return None if the binary relation is not an equivalence relation or a partitioning of the input set (e.g.: [{1, 3, 5, ...}, {2, 4, 6, ...}]) if it is an equivalence relation.
        return_list = []
        """

        pass
        
      
