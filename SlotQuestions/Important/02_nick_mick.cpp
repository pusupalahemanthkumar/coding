#include<bits/stdc++.h>
using namespace std;
long long int solve(long long int cap , long long int money , long long int p , long long int w , long long int cp ,  long long int cw){
    
    long long int tot =   0 ; 
    
   if(cp <=cw){
       
       long long int take  = money / cp ; 
       if(take >=min(cap , p)){
           take = min(cap , p) ;
           }
           tot = take;
           money -= (take * cp) ; 
           long long int tk = money/cw;
           if(tk >=w){
               tk = w;
           }
           tot = tot + tk;
       
   }
   
   else{
       long long int take  = money / cw ; 
       if(take >=w){
           take = w ;
           }
           tot = take;
           money -= (take * cw) ; 
           long long int tk = money/cp;
           if(tk >=min(p , cap)){
               tk = min(p , cap);
           }
           tot = tot + tk;
           
       
   }
   
   return tot;
}
    
    
int main(){
    
    
    long long int n,m,p,q,cp,cw,w;
    
    cin>>n>>m>>p>>w>>cp>>cw;
    long long int ans = 0 ;
   
    
    
    for(int i=0; i<=p; i++){
        long long int tot =  0;
        if( i *cp <=n){
            tot = i ; 
            long long int x = (n - (i*cp));
            x = x /cw;
            if(x >=w)x = w;
            tot = tot + x;
            
            tot = tot + solve( i , m , p - i , w - x , cp , cw);
            ans = max(ans , tot);
        }
    }
    cout<< ans;
}
