function metodoBiseccion(a, b, error)
	e = 0
    prev_e = 0
    err = 9999999999999

    n = 0
    while err > error
        prev_e = e
        e = (a + b) / 2

        printf("%d [%f, %f] %f %f\n", n, a, b, e, err)

        if sign(f(a)) <> sign(f(e))
            b = e
        else if sign(f(e)) <> sign(f(b))
            a = e
        else
            printf("Error\n")
            return
        end
        end

        n = n + 1

        err = abs(e - prev_e)
    end

    printf("%d [%f, %f] %f %f\n", n, a, b, e, err)
endfunction

function metodoSecante(x_0, x_1, error)
    x_2 = x_1 - ((x_1 - x_0) * f(x_1)) / (f(x_1) - f(x_0))

    printf("%f\n", x_0)
    printf("%f\n", x_1)
    printf("%f\n", x_2)

    while abs(x_1 - x_2) > error
        x_0 = x_1
        x_1 = x_2
        x_2 = x_1 - ((x_1 - x_0) * f(x_1)) / (f(x_1) - f(x_0))

        printf("%f\n", x_2)
    end

    printf("%f\n", x_2)
endfunction


function metodoRegulaFalsi(x_1, x_2, error)
    y_1 = f(x_1)
    y_2 = f(x_2)
    x_old = 9999999999999

    printf("(%f, %f)\n", x_1, y_1)
    printf("(%f, %f)\n", x_2, y_2)

    while abs(x_old - x_1) > error
        x = ((x_2 - x_1) / (y_2 - y_1)) * (0 - y_1) + x_1
        y = f(x)

        printf("(%f, %f)\n", x, y)

        x_old = x_1
        x_1 = x
        y_1 = y
    end
endfunction

function a = f(x)
    a = 
endfunction