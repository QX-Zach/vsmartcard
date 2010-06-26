#!/usr/bin/env python
# coding: utf-8

import sys
try:
    import pygtk
    pygtk.require("2.0")
    import gtk, gobject, glib
    import pango
except:
    sys.exit(1)

try:
    import pace
except:
    print "Could not import pace module, please install pyPACE" >> stderr
    sys.exit(1)

CVC = "\x7F\x21\x82\x01\x41\x7F\x4E\x81\xFA\x5F\x29\x01\x00\x42\x0D\x5A\x5A\x44\x56\x43\x41\x41\x54\x41\x30\x30\x30\x33\x7F\x49\x4F\x06\x0A\x04\x00\x7F\x00\x07\x02\x02\x02\x02\x03\x86\x41\x04\x19\xD1\x75\x45\xD3\xFE\x0B\x34\x3E\x7E\xE2\xAE\x4E\x2B\xC9\x2D\x51\x35\x1C\xC1\x17\xA4\x7F\xA9\x51\x9A\xDB\x1E\x40\x5E\xE6\xB8\x12\x12\x80\xBC\xC2\xFF\xF0\x35\x7A\x19\x7D\xE7\x39\xA7\xFD\x2E\xF0\x22\x10\xEF\x34\x3C\xDB\xE7\x9E\xF9\x4B\x8E\x28\x59\x1B\xB9\x5F\x20\x0B\x5A\x5A\x44\x4B\x42\x32\x30\x30\x30\x30\x52\x7F\x4C\x12\x06\x09\x04\x00\x7F\x00\x07\x03\x01\x02\x02\x53\x05\x00\x03\x01\xDF\x04\x5F\x25\x06\x01\x00\x00\x02\x01\x07\x5F\x24\x06\x01\x00\x00\x03\x03\x01\x65\x5E\x73\x2D\x06\x09\x04\x00\x7F\x00\x07\x03\x01\x03\x01\x80\x20\x75\xE0\xC4\xAC\x36\xC2\x5A\x33\xAC\x0E\x9A\x75\xEB\x79\x2A\x72\xF3\x31\xA5\x1E\x28\x63\x4E\xCC\x2E\xD6\x2E\x54\xF3\xC6\x93\xDA\x73\x2D\x06\x09\x04\x00\x7F\x00\x07\x03\x01\x03\x02\x80\x20\x18\x12\x65\x74\x49\xFC\xF1\xD3\xDA\xD8\x3D\x13\x14\x29\x17\x5C\x61\x8B\x21\xBA\xF0\xAF\x44\xAC\xE3\x8C\xB2\xC1\x2C\xEB\x2A\x56\x5F\x37\x40\x54\x0F\x85\x09\x12\xAB\xD3\x51\xF8\xF5\x56\x9B\x53\x4A\x5C\x8F\x64\x54\x5B\x51\xA7\x34\x70\xBE\x5A\xD2\x89\xC1\x9A\x5E\x13\x52\x53\xD3\xBB\x15\x52\x26\x21\x7B\x41\xE7\xF0\x68\xB3\x52\x3F\x3A\x63\x92\x22\xAF\x2B\x62\x8C\x39\x7D\x4F\xD4\x02\x1E\xDE\x00\xDC"

DESCRIPTION = "\x30\x82\x01\x90\x06\x0A\x04\x00\x7F\x00\x07\x03\x01\x03\x01\x01\xA1\x16\x0C\x14\x42\x75\x6E\x64\x65\x73\x64\x72\x75\x63\x6B\x65\x72\x65\x69\x20\x47\x6D\x62\x48\xA2\x24\x13\x22\x68\x74\x74\x70\x3A\x2F\x2F\x77\x77\x77\x2E\x62\x75\x6E\x64\x65\x73\x64\x72\x75\x63\x6B\x65\x72\x65\x69\x2E\x64\x65\x2F\x64\x76\x63\x61\xA3\x18\x0C\x16\x44\x65\x75\x74\x73\x63\x68\x65\x20\x4B\x72\x65\x64\x69\x74\x62\x61\x6E\x6B\x20\x41\x47\xA4\x13\x13\x11\x68\x74\x74\x70\x3A\x2F\x2F\x77\x77\x77\x2E\x64\x6B\x62\x2E\x64\x65\xA5\x82\x01\x13\x0C\x82\x01\x0F\x54\x61\x75\x62\x65\x6E\x73\x74\x72\x2E\x20\x37\x2D\x39\x0D\x0A\x31\x30\x31\x31\x37\x20\x42\x65\x72\x6C\x69\x6E\x0D\x0A\x69\x6E\x66\x6F\x40\x64\x6B\x62\x2E\x64\x65\x0D\x0A\x45\x72\xC3\xB6\x66\x66\x6E\x75\x6E\x67\x20\x65\x69\x6E\x65\x73\x20\x4B\x6F\x6E\x74\x6F\x73\x0D\x0A\x42\x65\x72\x6C\x69\x6E\x65\x72\x20\x42\x65\x61\x75\x66\x74\x72\x61\x67\x74\x65\x72\x20\x66\xC3\xBC\x72\x20\x44\x61\x74\x65\x6E\x73\x63\x68\x75\x74\x7A\x20\x75\x6E\x64\x20\x49\x6E\x66\x6F\x72\x6D\x61\x74\x69\x6F\x6E\x73\x66\x72\x65\x69\x68\x65\x69\x74\x2C\x20\x41\x6E\x20\x64\x65\x72\x20\x55\x72\x61\x6E\x69\x61\x20\x34\x2D\x31\x30\x2C\x20\x31\x30\x37\x38\x37\x20\x42\x65\x72\x6C\x69\x6E\x2C\x20\x30\x33\x30\x2F\x31\x33\x20\x38\x38\x39\x2D\x30\x2C\x20\x6D\x61\x69\x6C\x62\x6F\x78\x40\x64\x61\x74\x65\x6E\x73\x63\x68\x75\x74\x7A\x2D\x62\x65\x72\x6C\x69\x6E\x2E\x64\x65\x2C\x20\x68\x74\x74\x70\x3A\x2F\x2F\x77\x77\x77\x2E\x64\x61\x74\x65\x6E\x73\x63\x68\x75\x74\x7A\x2D\x62\x65\x72\x6C\x69\x6E\x2E\x64\x65\x0D\x0A\x45\x72\xC3\xB6\x66\x66\x6E\x75\x6E\x67\x20\x65\x69\x6E\x65\x73\x20\x4B\x6F\x6E\x74\x6F\x73\x0D\x0A"

at_chat_strings = [
        "Age Verification",
        "Community ID Verification",
        "Restrictied Identification",
        "Privileged Terminal",
        "CAN allowed",
        "PIN Managment",
        "Install Certificate",
        "Install Qualified Certificate",
        "Read DG 1",
        "Read DG 2",
        "Read DG 3",
        "Read DG 4",
        "Read DG 5",
        "Read DG 6",
        "Read DG 7",
        "Read DG 8",
        "Read DG 9",
        "Read DG 10",
        "Read DG 11",
        "Read DG 12",
        "Read DG 13",
        "Read DG 14",
        "Read DG 15",
        "Read DG 16",
        "Read DG 17",
        "Read DG 18",
        "Read DG 19",
        "Read DG 20",
        "Read DG 21",
        "RFU",
        "RFU",
        "RFU",
        "RFU",
        "Write DG 21",
        "Write DG 20",
        "Write DG 19",
        "Write DG 18",
        "Write DG 17"
]

def countBits(bitstring):
    numbits = 0
    for c in bitstring:
        for i in range(8):
            if ord(c) & 1 << i:
                numbits += 1
    return numbits

class CertificateDescriptionWindow(gtk.Window):

    def __init__(self, description):
        super(CertificateDescriptionWindow, self).__init__()

        self.description = description
        self.terms_str = pace.get_termsOfUsage(self.description)
        self.terms_array = self.terms_str.split("\n")

        self.successor = MainWindow(binchat, self) #FIXME: Get rid of global var

        self.connect("destroy", gtk.main_quit)
        self.set_default_size(480, 640)

        #Add a scrollbar if we must display lots of information
        self.scrolled_window = gtk.ScrolledWindow()
        self.scrolled_window.set_policy(gtk.POLICY_AUTOMATIC,
                gtk.POLICY_AUTOMATIC)
        self.add(self.scrolled_window)

        self.vb = gtk.VBox(False, 5)

        #Instruction label at the top of the window
        lblInstruction = gtk.Label(u"Informationen über den Dienst")
        lblInstruction.modify_font(pango.FontDescription("sans 18"))
        lblInstruction.set_alignment(0.5, 0.0)
        self.vb.pack_start(lblInstruction, False, False, 10)

        for s in self.terms_array:
            s = s.replace(", ", "\n")
            lbl = gtk.Label(s)
            lbl.set_alignment(0.0, 0.0)
            lbl.set_line_wrap(True)
            lbl.modify_font(pango.FontDescription("sans 14"))
            self.vb.pack_start(lbl, False, False, 2)

        #Add two buttons at the bottom of the window
        hbox = gtk.HBox(True)
        btnCancel = gtk.Button(stock="gtk-go-back")
        btnCancel.connect("clicked", self.cancel_clicked, None)
        hbox.pack_start(btnCancel)
        btnOK = gtk.Button(stock="gtk-go-forward")
        btnOK.connect("clicked", self.okay_clicked, None)
        hbox.pack_start(btnOK)
        self.vb.pack_start(hbox)

        self.scrolled_window.add_with_viewport(self.vb)
        self.show_all()

    def cancel_clicked(self, widget, data=None):
        pass

    def okay_clicked(self, widget, data=None):
        self.hide()
        self.successor.show_all()

class MainWindow(gtk.Window):

    def __init__(self, chat, predecessor):
        super(MainWindow, self).__init__()

        self.chat = chat
        self.predecessor = predecessor

        self.rel_auth = []
        for c in self.chat:
            self.rel_auth.append(ord(c))
        self.rel_auth_len = len(self.rel_auth)

        self.connect("destroy", gtk.main_quit)
        self.set_default_size(480, 640)
        self.access_rights = []

        #Add a scrollbar if we must display lots of access rights
        self.scrolled_window = gtk.ScrolledWindow()
        self.scrolled_window.set_policy(gtk.POLICY_AUTOMATIC,
                gtk.POLICY_AUTOMATIC)
        self.add(self.scrolled_window)

        self.vb = gtk.VBox(False, 5)

        #Instruction label at the top of the window
        lblInstruction = gtk.Label("Zugriffsrechte des Dienstes")
        lblInstruction.modify_font(pango.FontDescription("sans 18"))
        lblInstruction.set_alignment(0.5, 0.0)
        self.vb.pack_start(lblInstruction, True, True, 10)

        #Extract the access rights from the CHAT and display them in the window
        j = 0
        for i in range((self.rel_auth_len - 1) * 8 - 2):
            if (i % 8 == 0):
                j += 1
            if self.rel_auth[self.rel_auth_len - j] & (1 << (i % 8)):
                    chk = customCheckButton(at_chat_strings[i], i, self.vb)
                    self.access_rights.append(chk)

        #Add two buttons at the bottom of the window
        hbox = gtk.HBox(True)
        btnCancel = gtk.Button(stock="gtk-go-back")
        btnCancel.connect("clicked", self.cancel_clicked, None)
        hbox.pack_start(btnCancel)
        btnOK = gtk.Button(stock="gtk-go-forward")
        btnOK.connect("clicked", self.okay_clicked, None)
        hbox.pack_start(btnOK)
        self.vb.pack_start(hbox)

        #Display everything
        self.scrolled_window.add_with_viewport(self.vb)
#        self.show_all()

    def okay_clicked(self, widget, data=None):
        """ Check wether any access right have been deselected and modify the
            CHAT accordingly """

        for right in self.access_rights:
            if not right.is_active():
                idx = right.idx
                self.chat_array[len(self.chat) - 1 - idx / 8] ^= (1 << (idx % 8))

    def cancel_clicked(self, widget, data=None):
        self.hide()
        self.predecessor.show_all()

class customCheckButton(object):
    """This class provides a custom version of gtk.CheckButton.
       The main difference isthat the checkbox can be placed at the right
       side of the label and that we can store an index with the button"""

    def __init__(self, label, index, vbox):
        #Setup a label with the name of the access right
        self.lbl = gtk.Label(label)
        self.lbl.set_alignment(0.0, 0.5)
        self.lbl.set_padding(20, 0)
        self.lbl.modify_font(pango.FontDescription("sans 16"))

        #...and a checkbox on the right side of the label
        self.idx = index
        self.chk = gtk.CheckButton("")
        self.chk.set_active(True)
        self.chk.set_alignment(1.0, 0.5)

        #Insert the label and the checkbox in the vbox and add a seperator
        hbox = gtk.HBox()
        hbox.pack_start(self.lbl, True, True)
        hbox.pack_start(self.chk, False, False)
        vbox.pack_start(gtk.HSeparator())
        vbox.pack_start(hbox)

    def is_active(self):
        return self.chk.get_active()

if __name__ == "__main__":
    cvc = pace.d2i_CV_CERT(CVC)
    chat = pace.cvc_get_chat(cvc)
#    pace.cv_chat_dump(chat)
    binchat = pace.get_binary_chat(chat)
#    print "%r" % binchat
#    print "%d Bits set in CHAT" % countBits(binchat)

    desc = pace.d2i_CVC_CERTIFICATE_DESCRIPTION(DESCRIPTION)
    desc_txt = pace.get_termsOfUsage(desc)
    print desc_txt

#    w = MainWindow(binchat)
    w = CertificateDescriptionWindow(desc)
    gtk.main()
