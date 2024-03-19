// Name: Caleb Matherne
// Date: 5/10/2023
// Description: Programming assignment #1 (Page Replacement Algorithms)

// import the needed libraries
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

// declare variables that will be needed to be used globally
int* frames;                                                    // an array that will be allocated the needed space later to store the current working set of pages
int framecount;                                                 // the size to allocate for the current working set
int refarray[100] = {2, 8, 7, 2, 0, 3, 1, 7, 3, 1, 9, 3, 6, 1, 8, 4, 5, 1, 8, 8, \
3, 4, 4, 3, 4, 2, 0, 6, 6, 7, 0, 1, 0, 9, 3, 6, 4, 6, 8, 0, \
4, 6, 2, 3, 5, 7, 8, 0, 3, 2, 0, 0, 0, 4, 6, 9, 1, 4, 3, 8, \
8, 0, 0, 9, 7, 0, 7, 0, 9, 7, 7, 3, 8, 8, 9, 2, 7, 2, 1, 2, \
0, 9, 1, 1, 1, 5, 0, 7, 1, 4, 9, 1, 9, 5, 8, 4, 4, 7, 9, 6};    // reference array is initialized with default values

int FIFO(){                                                                     // FIFO page replacement algorithm (First In First Out)
    printf("\n\n-----=====FIFO=====-----\n");                                       // ~~~ print hear for the algorithm                     --- This portion of code detects when
    for (int frame = 0; frame < framecount; frame++) frames[frame] = -1;            // assign all frames to -1                                | there is a page fault and is
    int pagefaultcount = 0;                                                         // initialize page fault counter                          | present at the beginning of each
    int page;                                                                       // declare page variable to hold the current page         | of the other algorithms. I maybe
    int head = 0;                                                                   // initialize the head index                              | could've put it into it's own
    for (int i = 0; i < 100; i++){                                                  // for each page in the refarray                          | function to make things neater
        page = refarray[i];                                                             // assign the page                                    | code-wise, but some information
        printf("[%d]\n",page);                                                          // ~~~ print the page                                 | from previous for loops are needed
        for (int j = 0; j < framecount; j++) printf("| %d ",frames[j]); printf("|\n");  // ~~~ print the current frames array                 | in OPT() so I just left it as is.
        printf("  "); for (int n = 0; n < head; n++) printf("    "); printf("^\n");     // ~~~ print an indication for the head's location    |
        for (int j = 0; j < framecount; j++) {                                          // for each frame                                     |
            if (frames[j] == page) break;                                                   // if page is already in a frame, then break      |
            else if (j >= framecount-1) {                                                   // elif reached the end, we have a page fault   ---
                frames[head] = page;                                                            // set the frame at the head to the current page
                head = (head + 1) % framecount;                                                 // increment and mod the head position
                pagefaultcount++;                                                               // increment the page fault counter
            }                                                                               //
        }                                                                               //
    }                                                                               //
    return pagefaultcount;                                                          // return the number of page faults
}                                                                               //

int LRU(){                                                                      // LRU page replacement algorithm (Least Recently Used)
    printf("\n\n-----=====LRU=====-----\n");                                        // ~~~ print header for the algorithm                                                   --- Pretty much the same code as the other algorithms
    for (int frame = 0; frame < framecount; frame++) frames[frame] = -1;            // assign all frames to -1                                                                | for setup and detecting page faults.
    int pagefaultcount = 0;                                                         // initialize page fault counter                                                          |
    int page;                                                                       // declare page variable to hold the current page                                         |
    int agelist[framecount]; for (int i = 0; i < framecount; i++) agelist[i] = 0;   // declare and assign an age array to 0                                                   |
    int oldest;                                                                     // declare an oldest variable to hold the index of the frame that holds the oldest page   |
    for (int i = 0; i < 100; i++){                                                  // for each page in the refarray,                                                         |
        page = refarray[i];                                                             // assign the page                                                                    |
        printf("[%d]\n",page);                                                          // ~~~ print the page                                                                 |
        for (int j = 0; j < framecount; j++) {                                          // for each frame,                                                                    |
            if (frames[j] == page) {                                                        // if page is already in frames     --- Unlike the duplicate code in OPT(), this  |
                for (int k = 0; k < framecount; k++) agelist[k] = agelist[k] + 1;               // age the pages                  | duplicate code is still needed for the    |
                agelist[j] = 0;                                                                 // update the page age          --- algorithm to run.                         |
                break;                                                                          // break                                                                      |
            }                                                                               //                                                                                |
            else if (j >= framecount-1) {                                                   // if reached the end, we have a page fault                                     ---                             --- Page replacement method
                oldest = 0;                                                                     // set the oldest index                                                                                       | based on the algorithm
                for (int k = 1; k < framecount; k++){                                           // for each frame,                                                                                            |
                    if (agelist[k] > agelist[oldest]) oldest = k;                                   // if the frame is older than the page at the oldest index, oldest index becomes the index of that page   |
                }                                                                               //                                                                                                            |
                frames[oldest] = page;                                                          // set the frame with the oldest page index to the current page                                               |
                pagefaultcount++;                                                               // increment page fault count                                                                                 |
                for (int k = 0; k < framecount; k++) agelist[k] = agelist[k] + 1;               // age the pages                                                                                              |
                agelist[oldest] = 0;                                                            // update the page age                                                                                        |
            }                                                                               //                                                                                                              ---
        }                                                                               //
        for (int j = 0; j < framecount; j++) printf("| %d ",frames[j]); printf("|\n");  // ~~~ print the current frames array
        for (int j = 0; j < framecount; j++) printf("  %d ",agelist[j]); printf("\n\n");// ~~~ print the ages of each frame
    }                                                                               //
    return pagefaultcount;                                                      // return the number of page faults
}                                                                           //

int OPT(){                                                                      // OPT page preplacement algorithm (OPTimal)
    printf("\n\n-----=====OPT=====-----\n");                                        // ~~~ print header for the algorithm                                                                           --- Pretty much the same code as the other algorithms
    for (int frame = 0; frame < framecount; frame++) frames[frame] = -1;            // assign all frames to -1                                                                                        | for setup and detecting page faults.
    int pagefaultcount = 0;                                                         // initialize page fault counter                                                                                  |
    int page;                                                                       // declare page variable to hold the current page                                                                 |
    int distlist[framecount]; for (int i = 0; i < framecount; i++) distlist[i] = 0; // declare and assign a distance list to 0                                                                        |
    int furthest;                                                                   // declare a furthest variable to hold the index of the frame that holds the furthest page                        |
    for (int i = 0; i < 100; i++){                                                  // for each page in the refarray,                                                                                 |
        page = refarray[i];                                                             // set the page                                                                                               |
        printf("[%d]\n",page);                                                          // ~~~ print page                                                                                             |
        for (int j = 0; j < framecount; j++) printf("| %d ",frames[j]); printf("|\n");  // ~~~ print curent frames array                                                                              |
        for (int j = 0; j < framecount; j++) {                                          // for each frame,                                                                                            |
            if (frames[j] == page) {                                                    // if page is already in frames                                                                               |
                for (int k = 0; k < framecount; k++) distlist[k] = 0;                       // assign distlist to all 0                                     --- This isn't actually needed.           |
                for (int k = 0; k < framecount; k++){                                       // for each frame,                                                | It's just to update the distlist      |
                    for (int l = i; l < 100; l++){                                              // for each page reference after the current page,            | for printing. If this weren't here,   |
                        if (refarray[l] == frames[k]) break;                                        // if the page reference matches the page, break          | the distlist from last page fault     |
                        else distlist[k] = distlist[k] + 1;                                         // else, increment the page's distance in the distlist    | is used instead and the new           |
                    }                                                                           //                                                            | distances aren't shown. The actual    |
                }                                                                           //                                                              --- needed part of this code is below.    |
                break;                                                                      // break                                                                                                  |
            }                                                                           //                                                                                                            |
            else if (j >= framecount-1) {                                               // elif reached the end, we have a page fault                       --- Updates the distlist.               ---                 --- Page replacement method
                for (int k = 0; k < framecount; k++) distlist[k] = 0;                       // assign distlist to all 0                                       | It's the same code as above,                              | based on the algorithm
                for (int k = 0; k < framecount; k++){                                       // for each frame,                                                | but this is the one that is                               |
                    for (int l = i; l < 100; l++){                                              // for each page reference after the current page,            | actually needed for the                                   |
                        if (refarray[l] == frames[k]) break;                                        // if the page reference matches the page, break          | algorithm to run.                                         |
                        else distlist[k] = distlist[k] + 1;                                         // else, increment the page's distance in the distlist    |                                                           |
                    }                                                                           //                                                            |                                                           |
                }                                                                           //                                                              ---                                                           |
    // for each i page in refarray                              --- My psuedo(ish) code                                                                                                                                   |
        // for each j frame                                       | for updating the distlist.                                                                                                                            |
            // if page in frame j == page, break                  | This took me some time to                                                                                                                             |
            // else,                                              | get down into code. Leaving                                                                                                                           |
                // for each k frame,                              | in it here just because.                                                                                                                              |
                    // for each l page (from i to 100)            |                                                                                                                                                       |
                        // if refarray[l] == frames[k], break     |                                                                                                                                                       |
                        // else, distlist[k] ++                 ---                                                                                                                                                       |
                furthest = 0;                                                                       // assign furthest index to first frame                                                                               |
                for (int k = 1; k < framecount; k++){                                               // for each frame,                                                                                                    |
                    if (distlist[k] > distlist[furthest]) furthest = k;                                 // if the frame is further than the page at the furthest index, furthest index becomes the index of that page     |
                }                                                                                   //                                                                                                                    |
                frames[furthest] = page;                                                            // set the frame with the furthest page index to the current page                                                     |
                pagefaultcount++;                                                                   // increment the page fault count                                                                                     |
            }                                                                                   //                                                                                                                      ---
        }                                                                                   //
        for (int j = 0; j < framecount; j++) printf("  %d ",distlist[j]); printf("\n\n");   // ~~~ print the page distances in each frame
    }                                                                                   //
    return pagefaultcount;                                                          // return the number of page faults
}                                                                               //

int main(int argc, char* argv[]){                               // main
    if (argc == 1){                                                 // if no arguments given, print this error message (not about to tab everything over a mile away to fit this)
        printf("Incorect usage.\n\t./a.out {framecount} {seed}\n\n\tframecount : \tThe amount of frames to house the pages.\n\tseed : \tThe seed to generate random numbers from to fill the page-reference string.");
        return 1;                                                       // return with error
    }      
    framecount = atoi(argv[1]);                                     // convert ascii to int
    frames = malloc(framecount * sizeof(int));                      // allocate enough space for the frames
    if (argc == 3){                                                 // if both framecount and seed given          
        srand(atoi(argv[2]));                                           // convert the seed from ascii to int and set the seed
        for (int i = 0; i < 100; i++){                                  // for each index in the array
            refarray[i] = rand() % 10;                                      // set to random number
        }                                                               //
    }                                                               //
    printf("Algorithm\t#Page faults\n");                            // print header
    printf("FIFO\t\t%d\nLRU\t\t%d\nOPT\t\t%d",FIFO(),LRU(),OPT());  // print results
    return 0;                                                       // return normally
}                                                               //