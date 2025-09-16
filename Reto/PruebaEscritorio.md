## Prueba de Escritorio - Reto 1 (Caso A: Sustentación y Arrastre)

### Objetivo
Verificar paso a paso el cálculo de la Sustentación (L) y el Arrastre (D) de una aeronave y la decisión lógica sobre si puede volar (L >= peso).

### Fórmulas Utilizadas
- Sustentación: `L = 0.5 * rho * (V**2) * S * CL`
- Arrastre: `D = 0.5 * rho * (V**2) * S * CD`
- Condición de vuelo: `Si L >= peso -> "El avión puede volar"`, en caso contrario no.

### Definición de Variables
| Variable | Tipo  | Rol | Descripción |
|----------|-------|-----|-------------|
| rho      | float | Entrada | Densidad del aire (kg/m^3) |
| V        | float | Entrada | Velocidad del avión (m/s) |
| S        | float | Entrada | Superficie alar (m^2) |
| CL       | float | Entrada | Coeficiente de sustentación |
| CD       | float | Entrada | Coeficiente de arrastre |
| peso     | float | Entrada | Peso del avión (N) |
| L        | float | Intermedia/Salida | Sustentación calculada (N) |
| D        | float | Intermedia/Salida | Arrastre calculado (N) |

Constantes implícitas:
- El factor `0.5` (1/2) presente en las ecuaciones aerodinámicas estándar para fuerzas dinámicas.

### Caso de Prueba 1 (Valores Nominales)
| Entrada | Valor |
|---------|-------|
| rho | 1.225 |
| V   | 70 |
| S   | 16 |
| CL  | 1.2 |
| CD  | 0.35 |
| peso| 12000 |

#### Cálculos Paso a Paso
1. `V**2 = 70^2 = 4900`
2. `0.5 * rho = 0.5 * 1.225 = 0.6125`
3. `0.6125 * 4900 = 3001.25`
4. `3001.25 * S = 3001.25 * 16 = 48020`
5. Sustentación: `L = 48020 * CL = 48020 * 1.2 = 57624 N`
6. Arrastre: `D = 48020 * CD = 48020 * 0.35 = 16807 N`
7. Comparación: `L (57624) >= peso (12000)` → Verdadero.

#### Resultado Esperado en Pantalla
```
La sustentación del avión son: 57624.0 N
El arrastre del avión son: 16807.0 N
El avión puede volar.
```

### Caso de Prueba 2 (No alcanza sustentación)
| Entrada | Valor |
|---------|-------|
| rho | 1.225 |
| V   | 40 |
| S   | 12 |
| CL  | 0.9 |
| CD  | 0.32 |
| peso| 25000 |

#### Cálculos
1. `V**2 = 40^2 = 1600`
2. `0.5 * rho = 0.6125`
3. `0.6125 * 1600 = 980`
4. `980 * S = 980 * 12 = 11760`
5. `L = 11760 * 0.9 = 10584 N`
6. `D = 11760 * 0.32 = 3763.2 N`
7. `L (10584) >= peso (25000)` → Falso.

#### Resultado Esperado
```
La sustentación del avión son: 10584.0 N
El arrastre del avión son: 3763.2 N
El avión no puede volar.
```

### Caso de Prueba 3 (L exactamente igual al peso)
Elegimos valores para que L = peso.
| Entrada | Valor |
|---------|-------|
| rho | 1.225 |
| V   | 50 |
| S   | 10 |
| CL  | 1.2 |
| CD  | 0.30 |
| peso| 22968.75 |

#### Cálculos
1. `V**2 = 50^2 = 2500`
2. `0.5 * rho = 0.6125`
3. `0.6125 * 2500 = 1531.25`
4. `1531.25 * S = 1531.25 * 10 = 15312.5`
5. `L = 15312.5 * CL = 15312.5 * 1.2 = 18375.0` ← Ajustamos peso para que coincida con L realmente.

(Nota: Reajustamos peso a 18375.0 para que el caso sea exacto.)

6. `D = 15312.5 * 0.30 = 4593.75`
7. `L (18375.0) >= peso (18375.0)` → Verdadero.

#### Resultado Esperado
```
La sustentación del avión son: 18375.0 N
El arrastre del avión son: 4593.75 N
El avión puede volar.
```

### Resumen Lógico
| Caso | L (N) | D (N) | Peso (N) | Condición | Mensaje |
|------|-------|-------|----------|-----------|---------|
| 1 | 57624.0 | 16807.0 | 12000 | L >= peso (V) | Puede volar |
| 2 | 10584.0 | 3763.2 | 25000 | L >= peso (F) | No puede volar |
| 3 | 18375.0 | 4593.75 | 18375.0 | L >= peso (V) | Puede volar |

### Observaciones
- La estructura del cálculo reutiliza el factor común `0.5 * rho * V^2 * S` para ambas fuerzas.
- Se valida correctamente la condición de vuelo con `if L >= peso`.
- Los valores muestran coherencia física: mayor velocidad y coeficiente elevan L y D.

### Conclusión
La lógica implementada en el caso A funciona correctamente para los escenarios probados (suficiente sustentación, insuficiente sustento y caso límite).

