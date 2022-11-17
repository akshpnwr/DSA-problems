#include<stdio.h>
#include<stdlib.h>
#include<conio.h>

struct Node {
    int data;
    struct Node* left;
    struct Node* right;
};

struct Node* createNode(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->left = NULL;
    newNode->right = NULL;

    return newNode;
}
// root - left - right
void preOrder(struct Node* node) {

if (node == NULL)
{
    return;
}

printf("%d",node->data);

preOrder(node->left);

preOrder(node->right);

}
// left - right - root
void postOrder(struct Node* node) {

    if (node == NULL)
    {
        return;
    }
    
    postOrder(node->left);

    printf("%d",node->data);

    postOrder(node->right);



}
// left - root - right
void inOrder(struct Node* node) {

    if (node == NULL)
    {
        return;
    }
    
    postOrder(node->left);

    
    postOrder(node->right);

    printf("%d",node->data);


}

int main() {

    struct Node* root = createNode(0);

    struct Node *n1 = createNode(1);
    struct Node *n2 = createNode(2);
    struct Node *n3 = createNode(3);
    struct Node *n4 = createNode(4);
    struct Node *n5 = createNode(5);
    struct Node *n6 = createNode(6);

    root->left = n1;
    root->right = n2;

    n1->left = n3;
    n1->right = n4;
    n2->left = n5;
    n2->right = n6;

    // preOrder(root);
    // postOrder(root);
    // inOrder(root);
    return 0;
}
