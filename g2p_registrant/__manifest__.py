# -*- coding: utf-8 -*-
#################################################################################
# Author      : Newlogic (<https://newlogic.com/>)
# Copyright(c): Newlogic
# All Rights Reserved.
#################################################################################
{
  "name"         :  "G2P registrant Module",
  "category"     :  "G2P",
  "version"      :  "0.0.1",
  "sequence"     :  1,
  "author"       :  "Newlogic",
  "website"      :  "https://newlogic.com/",
  "license"      :  "Other OSI approved licence",
  "description"  :  """
  G2P registrant Module
  ========================

  - 
  
  """,
  "depends"      :  ['base','mail'],
  "data"         :  [
                  'security/newlogic_security.xml',
                  'security/ir.model.access.csv',
                  'views/main_view.xml',
                  'views/registrants_view.xml',
                    ],
  'assets'       :  {},
  "demo"         :  [],
  "images"       :  [],
  "application"  :  True,
  "installable"  :  True,
  "auto_install" :  False,
}
