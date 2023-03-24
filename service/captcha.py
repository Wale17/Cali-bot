import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from twocaptcha import TwoCaptcha

def captcha_cracker():
    api_key = os.getenv('APIKEY_2CAPTCHA', '66a780879e183c8fc52eadd47e786180')

    solver = TwoCaptcha(api_key)

    try:
        result = solver.solve_captcha(
            site_key='6Ldw-M4ZAAAAAPfWvPnaPKe2pp2iIWYdOkRDm9XT',
            page_url='https://www.cali.gov.co/participacion/publicaciones/161718/radicacion-de-peticiones-quejas-y-reclamos/#')

    except Exception as e:
        sys.exit(e)

    else:
        return str(result)


from twocaptcha import TwoCaptcha

class TwoCaptcher:
        def solve_recaptcha_v2(self, sitekey, api_key):
            solver = TwoCaptcha(api_key)
            for i in range(0,10):
                try:
                    result = solver.solve_captcha(
                        sitekey=sitekey,
                        url='https://procesojudicial.ramajudicial.gov.co/tutelaenlinea')
                    return [True,result]
                except:
                    pass
            return [False,"failed 10 times"]
