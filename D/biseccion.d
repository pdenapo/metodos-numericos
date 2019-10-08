/* Programita para implementar el método de bisección
  Busca un cero de f en el intervalo [a,b]
 tol= tolerancia prescripta para detener el método numérico
 (si no sería un ciclo infinito)

  Versión en lenguaje D
  Compilar con
		
		dmd biseccion.d

  Hipótesis: las del teorema de Bolzano
 f(a) y f(b) deben tener signos opuestos
 f debe ser continua en [a,b]

  Usamos una llamada recursiva por motivos didácticos.
 (Es más fácil de entender) */

import std.math;
import std.stdio; 

alias real_function = real function( real);

real biseccion(real_function f,  real a, real b, real tol=1e-11, uint n=1)
{    
    // La variable n cuenta las iteraciones
    // tol especifica la tolerancia permitida 
    // al método numérico
    
    writeln("n= ",n,":Bisección en el intervalo", 
                  "[", a,",", b, "]");
    if (abs(b - a) < tol)
        return a;
    if (f(a) == 0)
        return a;
    if (f(b) == 0)
        return b;
    // Encontramos el punto medio del intervalo [a,b]
    real c = (a + b) / 2;
    if (f(c) == 0)
            return c;
    if (f(a) > 0)
    {
        if (f(b) > 0)
            throw new Exception ("Error: hipótesis!");     
        // Si llegamos acá, f(b)<0     
        if (f(c) > 0)
            // sabemos que f(b)<0 y f(c)>0
            return biseccion(f, c, b, tol,n + 1);
        else
            // sabemos que f(a)>0 y f(c)<0
            return biseccion(f, a, c, tol,n + 1);
    }
    else
    {
        // caso en que f(a)<0
        if (f(b) < 0)
            throw new Exception ("Error: hipótesis!");
        // si llegamos acá f(b)>0
        if (f(c) > 0)
            // sabemos que f(a)<0 y f(c)>0
            return biseccion(f, a, c,tol, n + 1);
        else
            // sabemos que f(b)>0 y f(c) <0
            return biseccion(f, c, b,tol, n + 1);
     }
}

real mi_funcion(real x )
{
        return x * x - 2;
}


real mi_funcion2(real x )
{
        return exp(x) - 2;
}


real mi_funcion3(real x )
{
        return  sin(x) - cos(x);
}


void main()
{
	// Ejemplo 1: calculemos la raíz cuadrada de 2 
	// encontrando una raíz de un polinomio

    real raiz_hallada = biseccion(&mi_funcion, 0, 2,1e-11);
    writeln("raiz_hallada=", raiz_hallada);
    writeln("valor exacto=", sqrt(2.0));

    // Otro ejemplo: calculemos el logaritmo de 2 como la inversa de la
    // exponencial

    raiz_hallada = biseccion(&mi_funcion2, 0, 2, 1e-11);
    writeln("raiz_hallada=", raiz_hallada);
    writeln("valor exacto=", log(2));

    // ejemplo 3: calculemos pi/4 resolviendo la ecuación
    // sin(x)=cos(x)

    raiz_hallada = biseccion(&mi_funcion3, 0, 3, 1e-12);
    writeln("raiz_hallada=", raiz_hallada);
    writeln("valor exacto=", PI_4);
}
