#include <stdio.h>
#include <stdlib.h> 
#define MAX 100

typedef struct {
    char id[6];
    int deadline;
    int profit;
}Job;  /*Structre datatype Job*/

void jobsequencingwithdeadline(Job jobs[],int n);

int minvalue(int x,int y)
{
    if(x<y) return x;
    return y;
}

int main() {
    int n, i;
    Job *jobs;

    printf("Enter the number of jobs: ");
    scanf("%d", &n);

    // allocate memory dynamically for jobs array
    jobs = (Job *) malloc(n * sizeof(Job));

    printf("Enter job details - id, deadline, profit - for each job:\n");
    for (i = 0; i < n; i++) {
        scanf("%s%d%d", jobs[i].id, &jobs[i].deadline, &jobs[i].profit);
    }

    Job temp;
    for (i = 1; i < n; i++) {
        for (int j = 0; j < n - i; j++) {
            if (jobs[j + 1].profit > jobs[j].profit) {
                temp = jobs[j + 1];
                jobs[j + 1] = jobs[j];
                jobs[j] = temp;
            }
        }
    }

    printf("\nJob details sorted by profit:\n");
    printf("%10s %10s %10s\n", "Job", "Deadline", "Profit");
    for (i = 0; i < n; i++) {
        printf("%10s %10d %10d\n", jobs[i].id, jobs[i].deadline, jobs[i].profit);
    }

    jobsequencingwithdeadline(jobs, n);
 
    // free dynamically allocated memory
    free(jobs);
    return 0;
}

void jobsequencingwithdeadline(Job jobs[],int n)
{
    int i,j,k,maxprofit;
    //filled time slot
    int filledTimeSlot = 0;
    //free time slot
    int timeslot[MAX];
    //find max deadline value
    int dmax=0;
    for(i=0;i<n;i++)
    {
        if(jobs[i].deadline> dmax)
        {
            dmax=jobs[i].deadline;
        }
    }
    //free time slots initially set to -1 [-1 denotes empty]
    for(i=1;i<=dmax;i++)
    {
        timeslot[i]=-1;
    }
    printf("dmax:%d\n",dmax);

    for(i=1;i<=n;i++)
    {
         k=minvalue(dmax,jobs[i-1].deadline);
         while(k>=1)
         {
            if(timeslot[k]==-1)
            {
                timeslot[k]=i-1;
                filledTimeSlot++;      
                break;
            }
            k--;
         }
         //if all time slots are filled then stop
         if (filledTimeSlot==dmax)
         {
            break;
         }
    }

//required jobs
printf("\nRequired Jobs: ");
for(i=1;i<=dmax;i++)
{
    printf("%s",jobs[timeslot[i]].id);
    if (i<dmax)
    {
        printf(" --> ");
    }
}
maxprofit=0;
for(i=1;i<=dmax;i++)
{
   maxprofit+=jobs[timeslot[i]].profit;
}
printf("\nMax Profit:%d\n",maxprofit);

}

 