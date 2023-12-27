    bisection_results = (it.bisection(f, 0, 1.5), it.bisection(f, 1.5, 3))
    newton_raphson_results = (
        it.newton_raphson(f, df_dx, 0, print_convergence=True),
        it.newton_raphson(f, df_dx, 3, print_convergence=True),
    )
    secant_method_results = (it.secant(f, 0, 1.5), it.secant(f, 1.5, 3))