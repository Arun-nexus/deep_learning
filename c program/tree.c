#include<stdio.h>
#include<stdlib.h>

struct node{
	int data;
	struct node*left,*right;
	

};

struct node*createnode(int d){
	struct node*newnode=(struct node*)malloc(sizeof(struct node));
	newnode->data=d;
	newnode->left=NULL;
	newnode->right=NULL;
    return newnode;

}

struct node*insert(struct node*root,int value){
	

	if(root==NULL){
		
		return createnode(value);
	
	}
	if(value<root->data){
		root->left=insert(root->left,value);
	}else{
       root->right=insert(root->right,value);
	}
	return root;

}

void inorder(struct node* root){
    if(root!=NULL){
    inorder(root->left);
    printf("%d",root->data);
	inorder(root->right);}
    }




int main(){
	struct node*root=NULL;
 int m,t;

	while(1){
		printf("enter the choice");
		scanf("%d",&m);

		switch(m){
			case 1:
			printf("enter the data");
			scanf("%d",&t);
			root=insert(root,t);
			break;
			case 2:
			inorder(root);
            break;
            case 3:
			printf("exiting...");
			return 0;

			default:
			printf("error");
			
		}
	}
}