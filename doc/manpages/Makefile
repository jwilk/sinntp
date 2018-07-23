# Copyright © 2009-2018
#   Piotr Lewandowski <piotr.lewandowski@gmail.com>,
#   Jakub Wilk <jwilk@jwilk.net>.
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License, version 2, as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

XSL = http://docbook.sourceforge.net/release/xsl/current/manpages/docbook.xsl
XSLTPROC = xsltproc --nonet --param man.charmap.use.subset 0

XML_FILES = $(wildcard *.xml)
MAN_FILES = $(XML_FILES:.xml=.1)

.PHONY: all
all: $(MAN_FILES)

%.1: %.xml
	$(XSLTPROC) $(XSL) $(<)
	perl -pi -e '/^[.]TH\b/ and s,"[0-9/]{10}","$(shell date +%F)",' $(@)

.PHONY: clean
clean:
	rm -f $(MAN_FILES)

.error = GNU make is required

# vim:ts=4 sts=4 sw=4 noet
