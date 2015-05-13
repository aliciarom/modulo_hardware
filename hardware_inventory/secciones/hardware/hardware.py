# -*- coding: utf-8 -*-

######################################################################################################################################################
#  @version     : 1.0                                                                                                                                #
#  @autor       : SUPERMAS-ARC                                                                                                                       #
#  @creación    : 2015-05-12                                                                                                                         #
#  @linea       : Maximo 150 chars                                                                                                                   #
######################################################################################################################################################

#OpenERP Imports
from osv import fields, osv
from datetime import datetime, date
import re
#Modulo ::
class hardware(osv.osv):
  STATUS = [
    ('active', 'Active'),
    ('inactive', 'Inactive'),
    ('repair', 'In repair'),
    ('warranty', 'In warranty'),
    ('donated', 'Donated'),
    ('discarded', 'discarded')
    
  ]
 
  ### //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// ###
  ###                                                                                                                                              ###
  ###                                                  Atributos basicos de un modelo OPENERP                                                      ###
  ###                                                                                                                                              ###
  ### //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// ###
  
  #Nombre del modelo
  _name = 'hardware'
  
  #Nombre de la tabla
  _table = 'hardware'
 
 
  _columns = {
        
    'key':fields.char("Key", size=10, required=True),
    'brad':fields.char("Brand", size=50, required=True),
    'model':fields.char("Model", size=50, required=False),
    'serial_number':fields.char("Serial Number", size=50, required=True),
    'description':fields.text("Descripcion"),
    # 'location':fields.char("Location", size=5, requires=True),
    'mac':fields.char("MAC Ethernet", size=50, required=False),
    'mac_wifi':fields.char("MAC Wi-Fi", size=50, required=False),
    'ram':fields.integer("RAM", required=False),
    'hd_capacity':fields.integer("HD Capacity", required=False),
    'last_maintenance_date':fields.date("Last Maintenance Date", required=False),
    'next_maintenance_date':fields.date("Next Maintenance", required=False),
    'status_dic':fields.selection(STATUS, 'Status'),
    'cost_hardware':fields.float('Cost Hardware', required=False),
    # 'status':fields.selection(
    #   (
    #     ('1', 'Active'),
    #     ('2', 'Inactive'),
    #     ('3', 'In repair'),
    #     ('4', 'In warranty'),
    #     ('5', 'Donated'),      
    #   ),
    #   'Status', required = False
    # ),
    
    'store' : fields.selection(
      (
        ( 'sm1', 'SM1'),
        ( 'sm2', 'SM2' ),
        ( 'sm3', 'SM3' ),
        ( 'sm4', 'SM4' ),
        ( 'sm5', 'SM5' ),
      ),
      'Location',	required = False,
    ),
  # =====Relaciones [one2many](o2m)=============#
    'dispositivo_m2o_id': fields.many2one(
      'cat_dispositivos',
      'Device Type',
      required = True
    ),
        # 'software_m2o_id' : fields.many2one(
        #   'software',
        #   'Software',
        #   required = False
        # ),   
  }

#se cierra la clase
hardware() 


