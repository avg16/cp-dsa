#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
   int *minTime, *maxTime;

   int d, sumTime;
   cin >> d >> sumTime;
   minTime = new int[d];
   maxTime = new int[d];

   int sumMin = 0, sumMax = 0;
   for ( int i = 0; i < d; i++ )
   {
      cin >> minTime[i] >> maxTime[i];
      sumMin += minTime[i];
      sumMax += maxTime[i];
   }
 
   if ( sumTime < sumMin || sumTime > sumMax )                     
   {
      cout << "NO\n";
   }
   else
   {
      cout << "YES\n";
      int deficit = sumTime - sumMin;                               
      for ( int i = 0; i < d; i++ )
      {
         if ( deficit > 0 )                                         
         {                                                          
            int extra = min( deficit, maxTime[i] - minTime[i] );    
            deficit -= extra;                                       
            cout << minTime[i] + extra << " ";
         }
         else
         {
            cout << minTime[i] << " ";
         }
      }
   }

   delete [] minTime;
   delete [] maxTime;
}