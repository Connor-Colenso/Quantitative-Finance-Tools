import tools.american_options.binomial_method.american_call_option as american_call
import tools.american_options.binomial_method.american_put_option as american_put
import tools.american_options.binomial_method.american_chooser_option as american_chooser


def main():

    price = american_chooser.binomial_method(sigma=0.3, M=4, T=1.5, S=100, r=0.05, K=10, method=1)
    print(price)


if __name__ == '__main__':
    main()
