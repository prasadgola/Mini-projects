#include<stdlib.h>
#include<stdio.h>
#include<stack>
struct Node
{
	int data;
	struct Node* next;
};
struct Node* head;
void Reverse(){
	if(head == NULL) 
		return;
	stack<struct Node*> S;
	Node* temp = head;
	while(temp != NULL)
	{
		S.push(temp);
		temp= temp->next;
	}	
	temp = Stop(); head = temp;
	S.pop();
	while(!S. empty())
	{
		temp->next = S.top();
		S.pop();
		temp = temp->next;
	}
	temp->next = NULL;
}
void Insert(int x)
{
	struct Node* temp = (struct Node*)malloc(sizeof(struct Node));
    temp->data = x;
    temp->next = head;
    head = temp;
}
void print()
{
	struct Node* temp = head;
    printf("List is: ");
    while(temp != NULL)
    {
    	printf(" %d", temp->data);
        temp = temp->next;
    }
    printf("\n");
}
void main()
{
	head = NULL;
    printf("numbers\n");
    int n, i,x;
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
    	printf("enter value \n");
        scanf("%d",&x);
        Insert(x),
        Reverse();
        print();
    }
}