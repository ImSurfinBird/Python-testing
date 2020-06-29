# Informatik I, Übung 07

## Aufgabe 1: Rekursion/Iteration

	public static int compute(int n){ 
	    return computeInternal(n,1,1); 
	}
    private static int computeInternal(int n, int i, int res){ 
        if(i == n) 
            return res; 
        return computeInternal(n, i+1, res+i+i+1);
    } 

### 1. Betrachten Sie den Aufruf compute(5) und erstellen Sie ein rekursives Ablaufprotokoll für den zugehörigen Aufruf der Methode computeInternal.

Rekursives Ablaufprotokoll:
1. n = Eingabewert, i = 1, res = 1
2. if i = n -> res wird zurückgegeben (Programmende), sonst -> 3.
3. res = res + 2*i + 1
4. i = i + 1
5. -> 2.

Für compute(5):
1. n = 5, i = 1, res = 1
2. i != n
3. res = 4
4. i = 2
5. i != n
6. res = 9
7. i = 3
8. i != n
9. res = 16
10. i = 4
11. i != n
12. res = 25
13. i = 5
14. i = n
15. return 25

### 2.  Welche Funktion f(n) berechnet compute(int n)?

f(n) = $n^2$

### 3.  Formulieren Sie compute(int n) iterativ, geben Sie dazu Java-Code für die Methode an. Die Idee zur Berechung von f(n) soll dabei erhalten bleiben.

    public static int compute(int n){
        int res = 0;
        while(n>0){
            res = res + n + n - 1;
            n--;
        }
        return n; 
    }

## Aufgabe 2: Suchen

Formulieren Sie jeweils eine Idee und eine Methode in Java-Code zur Lösung der folgenden speziellen Suchprobleme. Fassen Sie Ihre Lösungen in einer Datei zusammen.

### 1. 

Gegeben ist eine Folge ganzer Zahlen (f0,f1,...,fn−1) mit mindestens einem Folgenglied. 

Gesucht ist ein $i ∈{0,...,n−1}$ mit $fi ≥ fj$ für alle $j ∈{0,...,n−1}.$

Idee: 
1. Sei j = 0. 
2. Wenn $f_i <= f_j$ setze $i=j$. 
3. j + 1
4. Wenn $j != n-1$ -> 2.
5. return i


    public static int MAX_Index(int[] f){
        int i = 0;
        for (int j = 0; j<f.length; j++){
            if(f[i]<=f[j]){
                i = j;
            }
        }
        return i;
    }

### 2. 

Gegeben ist eine Folge ganzer Zahlen (f0,f1,...,fn−1) mit mindestens einem Folgenglied. 

Gesucht ist ein i ∈ {0,...,n−1} mit |fi −f((i+1) mod n)| ≥ |fj −f((j+1) mod n)| für alle j ∈{0,...,n−1}.

Idee: 
1. Sei j = 0.
2. Wenn $| f_i - f_(i+1) mod n | <= | f_j - f_(j+1) mod n |$ setze $i=j$. 
3. j + 1
4. Wenn $j != n-1$ -> 2.
5. return i


    public static int MAX_Index_Tuple_mod_n(int[] f){
        int i = 0;
        int n = f.length;
        for (int j = 0; j<(n-1); j++){
            if(Math.abs((f[i]-f[i+1]) % n) <= Math.abs((f[j]-f[j+1]) % n)){
                i = j;
            }
        }
        return i;
    }

### 3.

Gegeben ist eine Folge ganzer Zahlen (f0,f1,...,fn−1) mit mindestens einem Folgenglied. 

Gesucht ist ein i ∈ {0,...,n − 1} mit Pn−1 j=0 |fi − fj| ≤Pn−1 j=0 |fk − fj| für alle k ∈{0,...,n−1}. 

Idee:
1. Sei j = 0.
2. Berechne $Sum(j=0 bis n-1) von |f_i - f_j|$
3. Wenn $Sum(k=k+1 bis n-1) von |f_k - f_(n-1)|$ $<=$ $Sum(k=0 bis n-1) von |f_i - f_(n-1)|$ -> i = k
4. k + 1
5. Wenn k<n -> 2.
6. return i


    public static int Min_Sequence(int[] f){
        int i = 0;
        int n = f.length;
        sum1 = Abs_Sum(f, i, n-1)
        for (int k = 0; k<n; k++){
            sum2 = Abs_Sum(f, k, n-1);
            if (sum2 <= sum1){
                i = k;
                sum1 = sum2;
            }
        }
        return i;
    }
    
    private static int Abs_Sum(int[] d, int min, int max){
        for (int sum = d[min]; min<max; min++){
            sum = sum + Math.abs(d[min] - d[min+1])
        }
        return sum;
    }        
