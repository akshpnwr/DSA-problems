#include<stdio.h>
#include<stdlib.h>


struct node {
    int data;
    struct node *next;
};

struct node *head = NULL;

void display() {
    struct node *ptr = head;

    printf("\nThe linked list is : ");
    while (ptr!=NULL) {
        printf("%d -> ",ptr->data);
        ptr = ptr->next;
    }
    printf("NULL");

}

void createList(int n) {

    int data;
    struct node *n1 = (struct node*) malloc(sizeof(struct node));
    printf("Enter data : ");
    scanf("%d",&data);

    n1->data = data;
    n1->next = NULL;

    head = n1;

    struct node *ptr = head;

    for (int i = 2; i <=n; i++)
    {
        struct node* new = (struct node*) malloc(sizeof(struct node));
        printf("Enter data : ");
        scanf("%d",&data);
        new->data = data;
        new->next = NULL;

        ptr->next = new;
        ptr = ptr->next;
    }

}

void insertAtEnd(int data) {

    struct node *ptr = head;

    while(ptr->next!=NULL) {
        ptr=ptr->next;
    }

    struct node *new = (struct node*) malloc(sizeof(struct node));
    new->data = data;
    new->next = NULL;

    ptr->next = new;
    ptr = ptr->next;
}

void insertAtBeginning(int data) {

struct node* ptr = head;

struct node* new = (struct node*) malloc(sizeof(struct node));

new->data = data;
// new->next = NULL;

new->next = ptr;
head = new;

}

int main() {

    
    int num_nodes, data;
    printf("Enter number of nodes : ");
    scanf("%d",&num_nodes);

    createList(num_nodes);

    printf("Enter data to insert : ");
    scanf("%d",&data);
    
    // insertAtEnd(n);

    // insertAtBeginning(n);
    display();
    return 0;
}
