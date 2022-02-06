import tools.option_pricing.american_options.binomial_method.american_call_option as american_call
import tools.option_pricing.american_options.binomial_method.american_put_option as american_put
import tools.option_pricing.american_options.binomial_method.american_chooser_option as american_chooser

from tools.utility.correlation_matrix import correlation_matrix_generator


def main():
    # price = american_chooser.binomial_method(sigma=0.3, M=4, T=1.5, S=100, r=0.05, K=10, method=1)
    # print(price)

    df = correlation_matrix_generator(securities=['AAPL', 'MSFT', 'NVDA'], period='1y', visual=True,
                                      img_name='image_dump/correlation_matrix', interval='1d')
    print(df)


if __name__ == '__main__':
    main()
