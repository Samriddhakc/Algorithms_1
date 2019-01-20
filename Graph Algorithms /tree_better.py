import pdb
import time

class BinarySearchTree:

	'''a Binary Search Tree example'''
	min_global=None
	def __init__(self,root,left=None,right=None):

		'''intialize variables'''

		self.curr=root
		self.left=left
		self.right=right

	def val(self):

		'''return the value of  the tree'''

		return self.curr

	def search_min_right(self,root):

		'''search minimum in the right sub tree'''
		self._search_min_right(root,root)


	def _search_min_right(self,min,root):
		global min_global
		if root.curr<min.curr:
			min=root
			min_global=min
		if root.left!=None:
			self._search_min_right(min,root.left)
		if root.right!=None:
			self._search_min_right(min,root.right)




	def delete(self,target):
		iter=self
		prev=None
		self._delete(iter,target,prev)


	def _delete(self,iter,target,prev):
			global min_global
			if iter!=None:
				if iter.curr==target:
					if iter.right==None and iter.left==None:
						if(prev.right==iter):
							prev.right=None
						elif(prev.left==iter):
							prev.left=None
					elif iter.right!=None and iter.left==None:
						prev.right=iter.right
					elif iter.right==None and iter.left!=None:
						prev.left=iter.left
					else:
						self.search_min_right(iter)
						if(prev.right==iter):
							prev.right=min_global
							min_global.left=iter.left
						elif(prev.left==iter):
							prev.left=min_global
							min_global.right=iter.right

				else:
					if iter.curr<target:
						self._delete(iter.right,target,iter)
					else:
						self._delete(iter.left,target,iter)
			else:
				print("Not Found")

	# def delete_with_while(self,target):


	def search_with_while(self,add_val):
		iter=self
		while(iter.left!=None or iter.right!=None):
			if(add_val==iter.curr):
				return True
			else:
				if(add_val<iter.curr):
					if (iter.left!=None):
						iter=iter.left
					else:
						return False
				else:
					if (iter.right!=None):
						iter=iter.right
					else:
						return False
		if iter.curr==add_val:
			return True
		else:
			return False


	def search(self,target):
		iter=self
		val=self._search(iter,target)
		return val

	def _search(self,iter,target):
		if iter.curr==target:
			return True
		else:
			if (iter.left!=None or iter.right!=None):
				if(iter.curr<target):
					return self._search(iter.right,target)
				else:
					return self._search(iter.left,target)
			else:
				return False

	def add(self,add_val):

		'''add value to the binary tree without using recursion'''

		iter=self
		while(iter.left!=None or iter.right!=None):
			if(add_val<iter.curr):
				if (iter.left!=None):
					iter=iter.left
				else:
					iter.left=BinarySearchTree(add_val)
					break
			else:
				if (iter.right!=None):
					iter=iter.right
				else:
					self.left=BinarySearchTree(add_val)
					break
		if add_val<iter.curr:
			iter.left=BinarySearchTree(add_val)
		else:
			iter.right=BinarySearchTree(add_val)


	def print_pre_order(self,req_lis):
		iter2=self
		self._print_pre_order(iter2,req_lis)

	def _print_pre_order(self,iter,req_lis):
		req_lis.append(iter.curr)
		if(iter.left!=None):
			self._print_pre_order(iter.left,req_lis)
		if(iter.right!=None):
			self._print_pre_order(iter.right,req_lis)

	def print_post_order_2(self):

		'''using stack and while loop'''
		s1=[]
		s2=[]
		s1.append(self)
		while s1:
			el=s1.pop()
			s2.append(el)
			if el.left:
				s1.append(el.left)
			if el.right:
				s1.append(el.right)
		while s2:
			print(s2.pop().curr)




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
	tree1.print_post_order_2()
	tree1.delete(9)
	print(" ")
	tree1.print_post_order_2()
	# time4=time.time()
	# req_lis=[]
	# tree1.print_pre_order(req_lis)
	# time1=time.time()
	# print(tree1.search(9))
	# print(tree1.search(100))
	# time2=time.time()
	# print(tree1.search_with_while(9))
	# print(tree1.search_with_while(100))
	# time3=time.time()
	# print(req_lis)
	# print(time4-time0)
	# print(time2-time1)
	# print(time3-time2)
main()
