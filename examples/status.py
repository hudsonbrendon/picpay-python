from picpay import PicPay
from decouple import config


picpay = PicPay(
    x_picpay_token=config("X_PICPAY_TOKEN"), x_seller_token=config("X_SELLER_TOKEN")
)

status = picpay.status(reference_id=102030)

print(status)
