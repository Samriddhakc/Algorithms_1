import time 
class node:

	'''a node for any tree '''

	def __init__(self,cur_val,right=None,left=None):
		self.val=cur_val
		self.right=right
		self.left=left

	def get_val(self):
		return self.val

	def set_left(self,node_left):
		self.left=node_left

	def set_right(self, node_right):
		self.right=node_right

	def get_right(self):
		return self.right

	def get_left(self):
		return self.left



class BinarySearchTree:

	'''a Binary Search Tree example'''

	def __init__(self,root,left=None,right=None):
		self.curr=node(root,left,right)

	def add(self,add_val):
		iter=self.curr
		self._add(iter, add_val)

	def _add(self,iter,add_val):
		if (iter.get_val()<add_val):
			if iter.get_left()==None:
				iter.set_left(node(add_val))
			else:
				self._add(iter.get_left(),add_val)
		else:
			if iter.get_right()==None:
				iter.set_right(node(add_val))
			else:
				self._add(iter.get_right(),add_val)


	def print_pre_order(self,req_lis):
		iter2=self.curr
		self._print_in_order(iter2,req_lis)

	def _print_pre_order(self,iter2,lis):
		lis.append(iter2.get_val())
		if (iter2.get_left()!=None):
			self._print_pre_order(iter2.get_left(),lis)
		if (iter2.get_right()!=None):
			self._print_pre_order(iter2.get_right(),lis)

	def print_post_order(self,req_lis):
		iter2=self.curr
		self._print_post_order(iter2,req_lis)

	def _print_post_order(self,iter3,lis):
		if (iter3.get_left()!=None):
			self._print_post_order(iter3.get_left(),lis)
		if (iter3.get_right()!=None):
			self._print_post_order(iter3.get_right(),lis)
		lis.append(iter3.get_val())


	def print_in_order(self,req_lis):
		iter2=self.curr
		self._print_in_order(iter2,req_lis)

	def _print_in_order(self,iter4,lis):
		if (iter4.get_left()!=None):
			self._print_post_order(iter4.get_left(),lis)
		lis.append(iter4.get_val())
		if (iter4.get_right()!=None):
			self._print_post_order(iter4.get_right(),lis)


def main():

	print("Basic Tree example")
	tree1=BinarySearchTree(11)
	time0=time.time()
	tree1.add(13)
	tree1.add(9)
	tree1.add(10)
	tree1.add(8)
	tree1.add(14)
	tree1.add(12)
	time1=time.time()
	req_lis=[]
	tree1.print_in_order(req_lis)
	print(req_lis)
	print(time1-time0)
main()
