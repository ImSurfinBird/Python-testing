# Informatik I, Übung 06

## Aufgabe 1: TypeCasting

	public class TypeCasting { 
		public static void main(String[] args){ 
			short a=73; 
			short b=219; 
			short c=(short) (a+b); 
			int d=(byte) c; 
			short e=-3; 
			int f=(char) e; 
			int g=1; 
			int h=4; 
			double i=g/h*4.0;

			System.out.println(a); 
			System.out.println(b); 
			System.out.println(c); 
			System.out.println(d); 
			System.out.println(e); 
			System.out.println(f); 
			System.out.println(g); 
			System.out.println(h); 
			System.out.println(i);
		}
	}

### 1. Welche Ausgabe produziert die main-Methode und warum? 

	73
	219
	292
	36 (c = 292 in binary: 100100100 -> in byte 00100100 = 36)
	-3
	65533 (char Representation von -3 = $65533)
	1
	4
	0.0 (1/4 = 0.25 -> in int = 0 -> *4.0 = 0 -> in double = 0.0  )

### 2.  Warum verlangt der Java-Compiler in Zeile 5 ein type casting?

## Aufgabe 2

Es sei $a = (a_0,a_1,...,a_(n−1))$ eine n-stellige Binärziffernfolge mit $a_i ∈{0,1}$. Die Ableitung von a ist die n-stellige Binärziffernfolge b = (b0,b1,...,bn−1) mit bi ∈{0,1}, deren Ziffern folgendermaßen entstehen.

Für i = 0, ..., n-1 gilt b_i = {0 falls i = 0 und a_i = 0 | 0 falls i>0 unf a_i = a_(i-1) | 1 sonst

### 1.

Für die erste Stelle: Ist mein Folgeglied gleich 1?
Für die restliche Folge: Ist mein derzeitiges Folgeglied ungleich dem vorherigen Folgeglied?

Die Ableitung gibt insofern Rückgabe darüber ob die Folge alterniert oder zwischenzeitlich Folgeglieder den selben Wert haben.

### 2.

    vod main int[] d{
        for (int i = d.length() - 1; i >= 0; i--){
            if (d[0] == 0 && i == 0){
                d[i] = 0;
            }
            else if (d[i] == d[i-1]){
                d[i] = 0;
            }
            else {
                d[i] = 1;
            }
        }
        return d;
    }

### 3.

Für i = 0, ..., n-1 gilt a_i = {b_0 falls i = 0|b_(i-1) falls i > 0 und a = 0|1 - b_(i-1) sonst}

### 4.

    vod main int[] d{
        for (int i = 1; i < d.length(); i++){
            if (d[i] == 0 && i > 0){
                d[i] = d[i-1];
            }
            else {
                d[i] = 1 - d[i-1];
            }
        }
        return d;
    }
