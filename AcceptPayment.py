import qrcode

#Taking UP ID as a input
upi_id = input("Enter your UP ID: ")

#upi://pay?pa=UPI_ID&pn=NAME&am=Amount&cu=CURRENCY&tn_MESSAGE

#Defining the payment URL based on the UPI ID and the payment app
#You can modify these URLs based on the payment apps you want to support

phonepe_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"
paytm_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"
googlepay_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"

#Create QR Codes for each payment app
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
googlepay_qr = qrcode.make(googlepay_url)

#Save the QR code to image file
phonepe_qr.save("phonepe_qr.png")
paytm_qr.save("paytm_qr.png")
googlepay_qr.save("googlepay_qr.png")

#Display the QR codes(you may need to install PIL/Pillow Library to display images)
phonepe_qr.show()
paytm_qr.show()
googlepay_qr.show()