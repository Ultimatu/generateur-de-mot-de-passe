import qrcode as qr
from PIL import Image

class GENER_qrcode:

     def createQrcode(self, donnee):
        donnee = str(donnee)
        Qrcode = qr.QRCode(
            error_correction=qr.constants.ERROR_CORRECT_H
        )
        # le message à insérer dans le qrcode
       
        Qrcode.add_data(donnee)

        # faire le qrcode
        Qrcode.make()

        # definir la couleur du qrcode
        Qrcolor = "black"


        # ajouter la couleur au qrcode
        Qrim = Qrcode.make_image(
            fill_color=Qrcolor,
            back_color="white").convert("RGB")
        for i in donnee:
            if i == ",":
                donnee = donnee.replace(i, "")
            if i in "/, &, ;":
                donnee = donnee.replace(i, "")
        self.im = ''.join(donnee)
        Qrim.save(f"{''.join(self.im)}.png")
        im = Image.open(f"{''.join(self.im)}.png")
        im.save(f"{''.join(self.im)}.gif")
        print("successfully...")
        return self.im
  
    