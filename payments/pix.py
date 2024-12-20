import uuid
import qrcode

class Pix:
    def __init__(self):
        pass

    def create_pix_payment(self, base_path=''):
        bank_payment_id = str(uuid.uuid4())
        qr_code_hash = f'qr_code_hash_{bank_payment_id}'
        qr_code_img = qrcode.make(qr_code_hash)
        qr_code_img.save(f'{base_path}/static/img/qr_code_hash_{bank_payment_id}.png')

        return {
            'bank_payment_id': bank_payment_id,
            'qr_code': qr_code_hash,
            'qr_code_path': f'../static/img/qr_code_hash_{bank_payment_id}.png'
        }

    def confirm_pix_payment(self):
        pass

