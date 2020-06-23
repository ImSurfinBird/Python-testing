# Informatik I, Übung 07

## Aufgabe 1: Java. Reverse Engineering

	public static foo(int x){ 
	    b = true; 
	    t = 2; 
	    while ((t*t <= x)&& b){ 
	        b = ((x%t) != 0); 
	        t++; 
	    } 
	    res = (b && (x != 1)); 
	    return res; 
	}

### 1. Vervollständigen Sie die Methode foo, indem Sie den Methodenkopf komplettieren und die Variablendeklarationen ergänzen.

	public static void foo(int x){ 
	    Boolean b = true; 
	    int t = 2; 
	    while ((t*t <= x) && b){ 
	        b = ((x%t) != 0); 
	        t++; 
	    } 
	    res = (b && (x != 1)); 
	    return res; 
	}

### 2.  Warum ist für jeden int-Wert x die Abbruchbedingung der Schleife irgendwann erfüllt?

Da t sich mit jeder Iteration der Schleife erhöht, erreicht t irgendwann einen Wert größer $x^0.5$ und (t*t <= x) ist false, was die Schleife beendet.

### 3. Beschreiben Sie die Funktionalität der Methode foo unter der Bedingung, dass x ein int-Wert mit x > 0 ist. D.h. welche Eigenschaften von x können aus dem Rückgabewert von foo gefolgert werden? 

Gibt foo True zurück existiert kein Wert t <= x^0.5 für den x%t = 0. Folglich ist x eine Primzahl.
Existiert ein solches t ist x keine Primzahl und foo gibt False zurück.
