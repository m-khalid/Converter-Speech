import frappe

safe_render = False
no_cache = 1

def get_context(context):
    if frappe.session.user == 'Guest':
        return context




# @frappe.whitelist()
@frappe.whitelist(allow_guest=True)
def get_converter_speach(text,lang):
    if frappe.session.user == 'Guest':
        pass
    from gtts import gTTS

    import os
    mytext = text

    language = lang

    myobj = gTTS(text=mytext, lang=language, slow=True)

    myobj.save("/home/frappe/frappe-bench/sites/erp1.trackintltrade.com/public/files/sound.mp3")
    return True
