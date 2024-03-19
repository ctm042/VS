/**
 * Name: Caleb Matherne
 * Date: 10/15/2022
 * Description: Program 5
 */
import java.text.spi.BreakIteratorProvider;
import java.util.Scanner;
import java.io.*;  

public class Main {
    static int getInfixPriority(char c){
        // switch(c) {
        //     case '(': return 4;
        //     case '^': return 3;
        //     case '*':
        //     case '/': return 2;
        //     case '+':
        //     case '-': return 1;
        //     default : return 0; 
        // }

        if (c == '('){return 4;}
        else if (c == '^'){return 3;}
        else if (c == '*' || c == '/'){return 2;}
        else if (c == '+' || c == '-'){return 2;}
        else return 0;
    }

    static int getStackPriority(char c){
        // switch(c) {
        //     case '^': 
        //     case '*': 
        //     case '/': return 2;
        //     case '+':
        //     case '-': return 1;
        //     default : return 0;
        // }

        if (c == '^' || c == '*' || c == '/'){return 2;}
        else if (c == '+' || c == '-'){return 1;}
        else return 0;
    }

    static boolean isOperand(char c){
        if (Character.isDigit(c)){
            return true;
        }
        return false;
    }

    static int eval(char operator, int a, int b){
        switch(operator){
            case '+': return a + b;
            case '-': return a - b;
            case '*': return a * b;
            case '/': return a / b;
            case '^': return (int)Math.pow(a, b);
            default : return -1;
        }
    }

    static String infixToPostfix(String infixString){
        // setting everything up
        Queue<Character> infixQueue = new Queue<>();
        Queue<Character> postfixQueue = new Queue<>();
        Stack<Character> operatorStack = new Stack<>();

        // enqueue each character into infixQueue
        char[] chars = infixString.toCharArray();
        for (char thing : chars){infixQueue.enqueue(thing);}

        // process the infixQueue
        while (!infixQueue.isEmpty()){
            // grab the next character
            char token = infixQueue.dequeue();

            // process operands (i.e. digits)
            if (isOperand(token)){postfixQueue.enqueue(token);}

            // process parenthesis
            else if (token==')'){
                char operator = operatorStack.pop();
                while (operator !='('){
                    postfixQueue.enqueue(operator);
                    operator = operatorStack.pop();
                }
            }

            //process operators (other than right parenthesis)
            else{
                // handle operators already on the operatorStack
                if (!operatorStack.isEmpty()){
                    char operator = operatorStack.peek();

                    // move operators with high priority into our postfixQueue
                    while (getStackPriority(operator) >= getInfixPriority(token)){
                        operator = operatorStack.pop();
                        postfixQueue.enqueue(operator);

                        // are there more operators on the operatorStack?
                        if (!operatorStack.isEmpty()){
                            // if so, grab it
                            operator = operatorStack.peek();
                        }
                        else{
                            // if not, exit out
                            break;
                        }
                    }
                }

                // push our new operator
                operatorStack.push(token);
            }
        }

        // NOTE: this is outside of our while loop above
        // this will unload the operator stack onto our postfixQueue
        while (!operatorStack.isEmpty()){
            char operator = operatorStack.pop();
            postfixQueue.enqueue(operator);
        }

        // transfer the postfixQueue contents into a string
        String postfix = "";
        while(!postfixQueue.isEmpty()){
            postfix += postfixQueue.dequeue();
        }

        // return that postfix string
        return postfix;
    }

    static int evalPostfix(String postfixString){
        // enqueue each character into postfixQueue
        Queue<Character> postfixQueue = new Queue<>();
        char[] chars = postfixString.toCharArray();
        for (char thing : chars){postfixQueue.enqueue(thing);}
        
        Stack<Integer> evalStack = new Stack<>();
        int finalResult=0;

        // process the postfixQueue
        while (!postfixQueue.isEmpty()){
            char token = postfixQueue.dequeue();

            // if token is a digit, throw it on the evalStack
            if (isOperand(token)){
                evalStack.push(Character.getNumericValue(token));

            }

            // otherwise, evaluate our sub-expression and
            // push the answer onto the evalStack
            else {
                System.out.println(token + " is an operator. Evaluating:");
                int a = evalStack.pop();

                int b = evalStack.pop();

                evalStack.push(eval(token, b, a));
            }
        }

        // if our evalStack is not empty after processing everything, then
        // return the final answer stored at the top
        if (!evalStack.isEmpty()){
            finalResult = evalStack.pop();
            return finalResult;
        }

        // otherwise report an error
        else{
            throw new ArithmeticException();
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter infix expression: ");
        String infixexpr = scanner.nextLine();

        String postfixexpr = infixToPostfix(infixexpr);
        System.out.println(postfixexpr);
        int result = evalPostfix(postfixexpr);

        System.out.println("Summary\n-------");
        System.out.println("  Infix: " + infixexpr);
        System.out.println("Postfix: " + postfixexpr);
        System.out.println(" Result: " + result);

    }
}
