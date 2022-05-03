# -*- coding: utf-8 -*-
#################################################################################
# Author      : New Logic (<https://newlogic.com/>)
# Copyright(c): New Logic
# All Rights Reserved.
#################################################################################
{
  "name"         :  "Newlogic Main Module",
  "category"     :  "NewLogic",
  "version"      :  "0.02",
  "sequence"     :  1,
  "author"       :  "New Logic",
  "website"      :  "https://newlogic.com/",
  "license"      :  "LGPL-3",
  "description"  :  """
  Newlogic Main Module
  ========================

  - 
  
  """,
  "depends"      :  ['base','mail'],
  "data"         :  [
                  'security/newlogic_security.xml',
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
