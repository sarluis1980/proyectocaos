# -*- coding: utf-8 -*-

def index():

    import json

    # Select all the records, to show how
    # datatables.net paginates.
    # Rows can't be serialized because they contain
    # an open database connection. Use as_list()
    # to serialize the query result.
    seleccionados = db(db.tbconfigura).select().first()
    if seleccionados==None:
        patron='0'
    else:
        patron= seleccionados.IdUbicacion
        fventa = json.dumps(db(db.tbtmp_linea_venta.IdUbicacion==patron).select(db.tbtmp_linea_venta.IdProducto,db.tbtmp_linea_venta.NombreProducto,db.tbtmp_linea_venta.Cantidad,db.tbtmp_linea_venta.ValorTotalProducto,db.tbtmp_linea_venta.ValorIva,db.tbtmp_linea_venta.PorcentajeDescuento,db.tbtmp_linea_venta.IdUbicacion).as_list())
    return dict(results=XML(fventa))


def seleccion_cliente():
    if not request.vars.txtcliente: return ''

    patron = request.vars.txtcliente.capitalize() + '%'
    seleccionados = [registro.NitEmpresa + '|' + registro.Empresa for registro in
                     db(db.tbClientes.Empresa.like(patron)).select()]

    return ''.join([DIV(k,
                 _onclick="jQuery('#txtcliente').val('%s')" % k,
                 _onmouseover="this.style.backgroundColor='yellow'",
                 _onmouseout="this.style.backgroundColor='white'"
                 ).xml() for k in seleccionados])

def Buscar_Nit_Cliente():
    if not request.vars.txtcliente: return ''

    patron = request.vars.txtcliente
    seleccionados = db(db.tbClientes.NitEmpresa==patron).select(db.tbClientes.Empresa).first()
    if seleccionados==None:
        patron='No existe el Cliente'
    else:
        patron=seleccionados.Empresa

    return patron

def seleccion_Producto():
    if not request.vars.txtproducto: return ''

    patron = request.vars.txtproducto.capitalize() + '%'
    seleccionados = [str(registro.IdProducto) + '|' + registro.Nombre + '|' + str(registro.PrecioUnitVenta) + '|' + str(registro.PorcentajeIva)  for registro in
                     db(db.tbProductos.Nombre.like(patron)).select()]

    return ''.join([DIV(k,
                 _onclick="jQuery('#txtproducto').val('%s')" % k,
                 _onmouseover="this.style.backgroundColor='yellow'",
                 _onmouseout="this.style.backgroundColor='white'"
                 ).xml() for k in seleccionados])

def Buscar_Producto():
    if not request.vars.txtproducto: return ''

    patron = request.vars.txtproducto
    seleccionados = db(db.tbProductos.IdProducto==patron).select().first()
    if seleccionados==None:
        patron='0'
    else:
        patron= str(seleccionados.IdProducto) + '|' + seleccionados.Nombre + '|' + str(seleccionados.PrecioUnitVenta) + '|' + str(seleccionados.PorcentajeIva)
    return patron

# Agraga registros a la tabla temporal de las facturas
def Agregar_Producto_tmp():

#db.tbtmp_linea_venta.IdProducto,db.tbtmp_linea_venta.NombreProducto,db.tbtmp_linea_venta.Cantidad,db.tbtmp_linea_venta.ValorTotalProducto,db.tbtmp_linea_venta.ValorIva,db.tbtmp_linea_venta.PorcentajeDescuento
    #try:
        cadenav = request.vars.cadenaproducto
        cadenav1 = cadenav.split("|")
        #Siempre se borra el producto que se va a agregar para garantizar que existe uno solo
        db(db.tbtmp_linea_venta.IdProducto==cadenav1[0],db.tbtmp_linea_venta.IdUbicacion==cadenav1[6]).delete()

        db.tbtmp_linea_venta.insert(IdProducto=cadenav1[0],
                        NombreProducto=cadenav1[1],
                        Cantidad=cadenav1[3],
                        ValorTotalProducto=cadenav1[2],
                        ValorIva=cadenav1[5],
                        PorcentajeDescuento=cadenav1[4],
                        IdUbicacion= cadenav1[6],
                        IdVenta=1
        )

    #except:
        #return "Error"
    #else:
       # return "Ok"

def Eliminar_linea_Producto():

    cadenav = request.vars.cadenaproducto
    cadenav1 = cadenav.split("|")
    #db.tbtmp_linea_venta.delete(IdProducto==cadenav1[0], IdUbicacion==cadenav1[1])
    db(db.tbtmp_linea_venta.IdProducto==cadenav1[0],db.tbtmp_linea_venta.IdUbicacion==cadenav1[0]).delete()


# Agraga registros a la tabla de las facturas
def Guardar_Factura():
    import datetime

    try:
        hora = datetime.datetime.now()
        strfecha = str(hora.year) + str(hora.month) + str(hora.day) + str(hora.hour) + str(hora.minute) + str(hora.second)
        #vrfecha = int(strfecha)
        #strfecha = '1'

        db.executesql('insert into tbLinea_Venta (IdVenta, IdProducto, IdUbicacion, Cantidad, ValorTotalProducto, ValorIva, PorcentajeDescuento) select ' + strfecha + ', IdProducto, IdUbicacion, Cantidad, ValorTotalProducto, ValorIva, PorcentajeDescuento from tbtmp_linea_venta where IdUbicacion="1";')

        db.executesql('update tbUbicacionProductosBA  set CantidadDisponible = CantidadDisponible - (select Cantidad from tbtmp_linea_venta where tbtmp_linea_venta.IdUbicacion = "1" and tbtmp_linea_venta.IdProducto = tbUbicacionProductosBA.IdProducto) where tbUbicacionProductosBA.IdUbicacion = "1" and tbUbicacionProductosBA.IdProducto in (select tbtmp_linea_venta.IdProducto from tbtmp_linea_venta where tbtmp_linea_venta.IdUbicacion = "1");')

        #db(db.tbtmp_linea_venta.IdUbicacion=="1").delete()
        # Creamos la factura en la tabla tbventas
        db.executesql('insert into tbVentas (IdVenta, numfactura, IdUbicacion, NitEmpresa, TotalVenta, TotalIva, IdEmpleado, Fecha, Hora, NoCuotas, FechaVence, Pagada, Anulada, Observacion) select ' + strfecha + ', ' + strfecha + ', IdUbicacion, NitEmpresa, TotalVenta, TotalIva, IdEmpleado, date("now", "localtime"), datetime("now", "localtime"), NoCuotas, FechaVence, "1", "0", Observacion from tbtmp_ventas where IdUbicacion="1";')

        # Limpia archivos temporales
        db(db.tbtmp_linea_venta.IdUbicacion=="1").delete()
        db(db.tbtmp_ventas.IdUbicacion=="1").delete()
    except:

        db.rollback()

    else:

        db.commit()

def Cargar_Configuracion():
# Función que devuelve la configuración de la aplicación
    seleccionados = db(db.tbconfigura).select().first()
    if seleccionados==None:
        patron='0'
    else:
        patron= seleccionados.idempresa + '|' + seleccionados.IdUbicacion + '|' + seleccionados.RepProd
    return patron
