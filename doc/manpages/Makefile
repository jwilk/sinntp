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

xsl = http://docbook.sourceforge.net/release/xsl/current/manpages/docbook.xsl
xsltproc = xsltproc --nonet --param man.charmap.use.subset 0

xml_files = $(wildcard *.xml)
man_files = $(xml_files:.xml=.1)

.PHONY: all
all: $(man_files)

%.1: %.xml
	$(xsltproc) $(xsl) $(<)
	perl -pi -e '/^[.]TH\b/ and s,"[0-9/]{10}","$(shell date +%F)",' $(@)

.PHONY: check
check: $(xml_files)
	xmllint --nonet --noout --valid $(^)

.PHONY: clean
clean:
	rm -f $(man_files)

.error = GNU make is required

# vim:ts=4 sts=4 sw=4 noet
