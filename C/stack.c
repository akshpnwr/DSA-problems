#include<stdio.h>
#include<stdlib.h>
#include<conio.h>

struct Node {
    int data;
    struct Node* next;
};

struct Node* TOP = NULL;

struct Node* createNode() {

    int data;
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    
    printf("\nEnter data : ");
    scanf("%d",&data);

    newNode->data = data;
    newNode->next = NULL;

    return newNode;
}

void push(struct Node* newNode) {

    if (TOP == NULL)
    {
        TOP = newNode;
    }

    else {

        newNode->next = TOP;
        TOP = newNode;

    }    

}

void display() {
    struct Node* ptr = TOP;

    printf("\nStack : ");
    while (ptr!=NULL)
    {
        printf("%d -> ",ptr->data);
        ptr = ptr->next;
    }
    printf("NULL");
    
}

int pop() {

    int poppedValue;

    if (TOP == NULL)
    {
        printf("\nNothin to DELETE!! OVERFLOW....Aborting!");
        exit(1);

    }
    
    else {

        struct Node* ptr = TOP;
        poppedValue = TOP->data;
        TOP = TOP->next;
        free(ptr);
        return poppedValue;

    }
    
}

int main() {


    struct Node* newNode1 = createNode();
    push(newNode1);
    struct Node* newNode2 = createNode();
    push(newNode2);
    struct Node* newNode3 = createNode();
    push(newNode3);

    display();

    printf("\nPopped : %d",pop());

    display();
    
return 0;
}
