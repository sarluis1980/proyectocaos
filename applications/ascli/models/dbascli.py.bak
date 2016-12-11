# -*- coding: utf-8 -*-
db.define_table('TbAbonosDeudas',
	db.Field('IdAbono', type='double', label=T(u'IdAbono'),comment='xxx'),
	db.Field('IdTabla', type='text', length=1, label=T(u'IdTabla'),comment='xxx'),
	db.Field('ConsecutivoFactura', type='double', label=T(u'ConsecutivoFactura'),comment='xxx'),
	db.Field('ValorAbono', type='double', label=T(u'ValorAbono'),comment='xxx'),
	db.Field('FechaPago', type='date', label=T(u'FechaPago'),comment='xxx')
	)
db.define_table('TbAhorrosDiarios',
	db.Field('IdAhorroDiario', type='double', label=T(u'IdAhorroDiario'),comment='xxx'),
	db.Field('Descripcion', type='string', length=30, label=T(u'Descripcion'),comment='xxx'),
	db.Field('Prioridad', type='text', length=1, label=T(u'Prioridad'),comment='xxx'),
	db.Field('Tipo', type='text', length=1, label=T(u'Tipo'),comment='xxx'),
	db.Field('Valor', type='double', label=T(u'Valor'),comment='xxx'),
	db.Field('IdEmpleado', type='string', length=15, label=T(u'IdEmpleado'),comment='xxx'),
	db.Field('Fecha_Modificacion', type='date', label=T(u'Fecha_Modificacion'),comment='xxx'),
	db.Field('Observacion', type='string', length=1000, label=T(u'Observacion'),comment='xxx'),
	db.Field('IdUbicacion', type='text', length=2, label=T(u'IdUbicacion'),comment='xxx')
	)
db.define_table('TbCambiosDevoluciones',
	db.Field('IdCambioDevolucion', type='double', label=T(u'IdCambioDevolucion'),comment='xxx'),
	db.Field('IdEmpleado', type='string', length=15, label=T(u'IdEmpleado'),comment='xxx'),
	db.Field('IdUbicacion', type='text', length=2, label=T(u'IdUbicacion'),comment='xxx'),
	db.Field('IdProducto', type='double', label=T(u'IdProducto'),comment='xxx'),
	db.Field('Cantidad', type='double', label=T(u'Cantidad'),comment='xxx'),
	db.Field('ValorTotal', type='double', label=T(u'ValorTotal'),comment='xxx'),
	db.Field('Fecha', type='date', label=T(u'Fecha'),comment='xxx'),
	db.Field('Hora', type='time', label=T(u'Hora'),comment='xxx'),
	db.Field('Causa', type='string', length=20, label=T(u'Causa'),comment='xxx'),
	db.Field('Observacion', type='string', length=1000, label=T(u'Observacion'),comment='xxx'),
	db.Field('DevolverDinero', type='text', length=1, label=T(u'DevolverDinero'),comment='xxx')
	)
db.define_table('TbCuentas',
	db.Field('IdCuenta', type='text', length=10, label=T(u'IdCuenta'),comment='xxx'),
	db.Field('NombreCuenta', type='string', length=100, label=T(u'NombreCuenta'),comment='xxx'),
	db.Field('Descripcion', type='string', length=500, label=T(u'Descripcion'),comment='xxx')
	)
db.define_table('TbLinea_AhorrosDiarios',
	db.Field('IdConsecutivoAhorro', type='double', label=T(u'IdConsecutivoAhorro'),comment='xxx'),
	db.Field('IdAhorroDiario', type='double', label=T(u'IdAhorroDiario'),comment='xxx'),
	db.Field('ValorIngreso', type='double', label=T(u'ValorIngreso'),comment='xxx'),
	db.Field('Fecha', type='text', length=10, label=T(u'Fecha'),comment='xxx'),
	db.Field('IdEmpleado', type='text', length=10, label=T(u'IdEmpleado'),comment='xxx')
	)
db.define_table('tbAdelantosPagosEmpleados',
	db.Field('IdPagoAdelanto', type='string', length=15, label=T(u'IdPagoAdelanto'),comment='xxx'),
	db.Field('IdEmpleado', type='string', length=15, label=T(u'IdEmpleado'),comment='xxx'),
	db.Field('FechaAdelanto', type='date', label=T(u'FechaAdelanto'),comment='xxx'),
	db.Field('IdPeriodo', type='text', length=8, label=T(u'IdPeriodo'),comment='xxx'),
	db.Field('ValorAdelanto', type='double', label=T(u'ValorAdelanto'),comment='xxx'),
	db.Field('Observacion', type='string', length=8000, label=T(u'Observacion'),comment='xxx')
	)
db.define_table('tbArticulos_Demandados',
	db.Field('IdProducto', type='string', length=20, label=T(u'IdProducto'),comment='xxx'),
	db.Field('NombreProducto', type='string', length=40, label=T(u'NombreProducto'),comment='xxx'),
	db.Field('Descripcion', type='string', length=8000, label=T(u'Descripcion'),comment='xxx'),
	db.Field('Contador', type='double', label=T(u'Contador'),comment='xxx')
	)
db.define_table('tbCaja',
	db.Field('Fecha', type='date', label=T(u'Fecha'),comment='xxx'),
	db.Field('IdUbicacion', type='text', length=2, label=T(u'IdUbicacion'),comment='xxx'),
	db.Field('ValorInicial', type='double', label=T(u'ValorInicial'),comment='xxx'),
	db.Field('ValorFinal', type='double', label=T(u'ValorFinal'),comment='xxx')
	)
db.define_table('tbCargo',
	db.Field('IdCargo', type='text', length=2, label=T(u'IdCargo'),comment='xxx'),
	db.Field('Nombre', type='string', length=30, label=T(u'Nombre'),comment='xxx'),
	db.Field('Descripcion', type='string', length=1000, label=T(u'Descripcion'),comment='xxx')
	)
db.define_table('tbCategorias',
	db.Field('IdCategoria', type='text', length=6, label=T(u'IdCategoria'),comment='xxx'),
	db.Field('NombreCategoria', type='string', length=20, label=T(u'NombreCategoria'),comment='xxx'),
	db.Field('Descripcion', type='string', length=1000, label=T(u'Descripcion'),comment='xxx')
	)
db.define_table('tbCierreCategorias',
	db.Field('IdCategoria', type='text', length=4, label=T(u'IdCategoria'),comment='xxx'),
	db.Field('IdEmpresa', type='string', length=15, label=T(u'IdEmpresa'),comment='xxx')
	)
db.define_table('tbCierresEmpleados',
	db.Field('IdCierre', type='string', length=20, label=T(u'IdCierre'),comment='xxx'),
	db.Field('IdEmpleado', type='string', length=15, label=T(u'IdEmpleado'),comment='xxx'),
	db.Field('Fecha', type='date', label=T(u'Fecha'),comment='xxx'),
    db.Field('Hora', type='time', label=T(u'Hora'),comment='xxx')
	)
db.define_table('tbCitas',
	db.Field('idCita', type='text', length=10, label=T(u'idCita'),comment='xxx'),
	db.Field('IdContacto', type='string', length=15, label=T(u'IdContacto'),comment='xxx'),
	db.Field('FechaCita', type='date', label=T(u'FechaCita'),comment='xxx'),
	db.Field('FechaAviso', type='date', label=T(u'FechaAviso'),comment='xxx'),
	db.Field('Cola', type='text', length=1, label=T(u'Cola'),comment='xxx'),
	db.Field('Descripcion', type='string', length=2000, label=T(u'Descripcion'),comment='xxx')
	)
db.define_table('tbClientes',
	db.Field('NitEmpresa', type='string', length=20, label=T(u'NitEmpresa'),comment='xxx'),
	db.Field('Empresa', type='string', length=40, label=T(u'Empresa'),comment='xxx'),
	db.Field('Direccion', type='string', length=40, label=T(u'Direccion'),comment='xxx'),
	db.Field('Telefono', type='string', length=20, label=T(u'Telefono'),comment='xxx'),
	db.Field('IdContacto', type='string', length=15, label=T(u'IdContacto'),comment='xxx'),
	db.Field('NombreContacto', type='string', length=45, label=T(u'NombreContacto'),comment='xxx'),
	db.Field('Mail', type='string', length=45, label=T(u'Mail'),comment='xxx'),
	db.Field('observacion', type='string', length=1000, label=T(u'observacion'),comment='xxx')
	)
db.define_table('tbCodigoGastos',
	db.Field('CodigoGasto', type='text', length=3, label=T(u'CodigoGasto'),comment='xxx'),
	db.Field('Nombre', type='string', length=40, label=T(u'Nombre'),comment='xxx')
	)
db.define_table('tbCodigoPermisos',
	db.Field('IdPermiso', type='text', length=2, label=T(u'IdPermiso'),comment='xxx'),
	db.Field('Descripcion', type='string', length=100, label=T(u'Descripcion'),comment='xxx'),
	db.Field('Remonerado', type='text', length=1, label=T(u'Remonerado'),comment='xxx')
	)
db.define_table('tbCompras',
	db.Field('Consecutivo', type='double', label=T(u'Consecutivo'),comment='xxx'),
	db.Field('IdCompra', type='string', length=15, label=T(u'IdCompra'),comment='xxx'),
	db.Field('IdProveedor', type='string', length=20, label=T(u'IdProveedor'),comment='xxx'),
	db.Field('Anulada', type='text', length=1, label=T(u'Anulada'),comment='xxx'),
	db.Field('TotalIva', type='double', label=T(u'TotalIva'),comment='xxx'),
	db.Field('TotalVenta', type='double', label=T(u'TotalVenta'),comment='xxx'),
	db.Field('IdEmpleado', type='string', length=15, label=T(u'IdEmpleado'),comment='xxx'),
	db.Field('Fecha', type='date', label=T(u'Fecha'),comment='xxx'),
	db.Field('FechaVence', type='date', label=T(u'FechaVence'),comment='xxx'),
	db.Field('IdUbicacion', type='text', length=2, label=T(u'IdUbicacion'),comment='xxx'),
	db.Field('Observacion', type='string', length=1000, label=T(u'Observacion'),comment='xxx'),
	db.Field('ValorDescuento', type='double', label=T(u'ValorDescuento'),comment='xxx'),
	db.Field('valorIvaDescuento', type='double', label=T(u'valorIvaDescuento'),comment='xxx'),
	db.Field('Pagada', type='text', length=1, label=T(u'Pagada'),comment='xxx')
	)
db.define_table('tbCotizaciones',
	db.Field('IdCotizacion', type='text', length=10, label=T(u'IdCotizacion'),comment='xxx'),
	db.Field('NitEmpresa', type='string', length=20, label=T(u'NitEmpresa'),comment='xxx'),
	db.Field('TotalVenta', type='double', label=T(u'TotalVenta'),comment='xxx'),
	db.Field('TotalIva', type='double', label=T(u'TotalIva'),comment='xxx'),
	db.Field('IdEmpleado', type='string', length=15, label=T(u'IdEmpleado'),comment='xxx'),
	db.Field('Fecha', type='date', label=T(u'Fecha'),comment='xxx'),
    db.Field('Hora', type='time', label=T(u'Hora'),comment='xxx'),
	db.Field('FechaVence', type='date', label=T(u'FechaVence'),comment='xxx'),
	db.Field('IdUbicacion', type='text', length=2, label=T(u'IdUbicacion'),comment='xxx'),
	db.Field('Observacion', type='string', length=8000, label=T(u'Observacion'),comment='xxx'),
	db.Field('PasadaParaVenta', type='text', length=1, label=T(u'PasadaParaVenta'),comment='xxx')
	)
db.define_table('tbDirectorio',	
	db.Field('IdContacto', type='string', length=15, label=T(u'IdContacto'),comment='xxx'),
	db.Field('Nombre', type='string', length=30, label=T(u'Nombre'),comment='xxx'),
	db.Field('PrimerApellido', type='string', length=20, label=T(u'PrimerApellido'),comment='xxx'),
	db.Field('SegundoApellido', type='string', length=20, label=T(u'SegundoApellido'),comment='xxx'),
	db.Field('DireccionCasa', type='string', length=50, label=T(u'DireccionCasa'),comment='xxx'),
	db.Field('TelefonoCasa', type='string', length=20, label=T(u'TelefonoCasa'),comment='xxx'),
	db.Field('Celular', type='string', length=30, label=T(u'Celular'),comment='xxx'),
	db.Field('Beeper', type='string', length=20, label=T(u'Beeper'),comment='xxx'),
	db.Field('Empresa', type='string', length=40, label=T(u'Empresa'),comment='xxx'),
	db.Field('TelefonoEmpresa', type='text', length=10, label=T(u'TelefonoEmpresa'),comment='xxx'),
	db.Field('IdGrupo', type='text', length=2, label=T(u'IdGrupo'),comment='xxx'),
	db.Field('Comentarios', type='text', length=10, label=T(u'Comentarios'),comment='xxx')
	)
db.define_table('tbEmpleados',
	db.Field('IdEmpleado', type='string', length=15, label=T(u'Identificación'),comment='xxx'),
	db.Field('Nombre', type='string', length=40, label=T(u'Nombre'),comment='xxx'),
	db.Field('PrimerApellido', type='string', length=15, label=T(u'Primer Apellido'),comment='xxx'),
	db.Field('SegundoApellido', type='string', length=15, label=T(u'Segundo Apellido'),comment='xxx'),
	db.Field('Direccion', type='string', length=50, label=T(u'Dirección'),comment='xxx'),
	db.Field('telefono', type='string', length=20, label=T(u'Teléfono'),comment='xxx'),
	db.Field('Mail', type='string', length=60, label=T(u'Mail'),comment='Ingrese el email', requires=IS_EMAIL()),
	db.Field('Observacion', type='string', length=4000, label=T(u'Observacion'),comment='xxx'),
	db.Field('FechaNacimiento', type='date', label=T(u'FechaNacimiento'),comment='xxx'),
	db.Field('IdUbicacion', type='text', length=2, label=T(u'IdUbicacion'),comment='xxx'),
	db.Field('IdEstado', type='text', length=2, label=T(u'IdEstado'),comment='xxx'),
	db.Field('IdCargo', type='text', length=2, label=T(u'IdCargo'),comment='xxx'),
	db.Field('SalarioBase', type='double', label=T(u'SalarioBase'),comment='xxx'),
	db.Field('FechaIng', type='date', label=T(u'FechaIng'),comment='xxx'),
	db.Field('Festringetiro', type='date', label=T(u'Festringetiro'),comment='xxx'),
	db.Field('NombrePadre', type='string', length=30, label=T(u'NombrePadre'),comment='xxx'),
	db.Field('NombreMadre', type='string', length=30, label=T(u'NombreMadre'),comment='xxx'),
	db.Field('EstadoCivil', type='string', length=20, label=T(u'EstadoCivil'),comment='xxx'),
	db.Field('NombreEsposo_a', type='string', length=30, label=T(u'NombreEsposo_a'),comment='xxx'),
	db.Field('NumeroHijos', type='double', label=T(u'NumeroHijos'),comment='xxx')
	)
db.define_table('tbEstado',
	db.Field('IdEstado', type='text', length=2, label=T(u'IdEstado'),comment='xxx'),
	db.Field('Nombre', type='string', length=20, label=T(u'Nombre'),comment='xxx'),
	db.Field('Descripcion', type='string', length=3000, label=T(u'Descripcion'),comment='xxx')
	)
db.define_table('tbFrases',
	db.Field('IdFrase', type='text', length=10, label=T(u'IdFrase'),comment='xxx'),
	db.Field('Descripcion', type='string', length=8000, label=T(u'Descripcion'),comment='xxx'),
	db.Field('fechaMuestra', type='datetime', label=T(u'fechaMuestra'),comment='xxx'),
	db.Field('HoraMuestra', type='date', label=T(u'HoraMuestra'),comment='xxx')
	)
db.define_table('tbGastos',
	db.Field('idGasto', type='text', length=10, label=T(u'idGasto'),comment='xxx'),
	db.Field('CodigoGasto', type='text', length=3, label=T(u'CodigoGasto'),comment='xxx'),
	db.Field('IdEmpleado', type='string', length=15, label=T(u'IdEmpleado'),comment='xxx'),
	db.Field('IdUbicacion', type='text', length=2, label=T(u'IdUbicacion'),comment='xxx'),
	db.Field('Valor', type='double', label=T(u'Valor'),comment='xxx'),
	db.Field('fecha', type='date', label=T(u'fecha'),comment='xxx'),
	db.Field('Descripcion', type='string', length=3000, label=T(u'Descripcion'),comment='xxx')
	)
db.define_table('tbGruposLlamadas',
	db.Field('idGrupo', type='text', length=2, label=T(u'idGrupo'),comment='xxx'),
	db.Field('Nombre', type='string', length=20, label=T(u'Nombre'),comment='xxx'),
	db.Field('Descripcion', type='string', length=1000, label=T(u'Descripcion'),comment='xxx')
	)
db.define_table('tbHoras_Trabajadas',
	db.Field('IdEmpleado', type='string', length=15, label=T(u'IdEmpleado'),comment='xxx'),
	db.Field('Fecha', type='date', label=T(u'Fecha'),comment='xxx'),
	db.Field('IdUbicacion', type='text', length=2, label=T(u'IdUbicacion'),comment='xxx'),
	db.Field('Hora_Entrada', type='time', label=T(u'Hora_Entrada'),comment='xxx'),
	db.Field('Hora_Salida', type='time', label=T(u'Hora_Salida'),comment='xxx'),
	db.Field('Dinero_Recaudado', type='double', label=T(u'Dinero_Recaudado'),comment='xxx')
	)
db.define_table('tbLineaOrdenesPedidosTrabajo',
	db.Field('IdOrdenPedidoTrabajo', type='text', length=10, label=T(u'IdOrdenPedidoTrabajo'),comment='xxx'),
	db.Field('idProducto', type='double', label=T(u'idProducto'),comment='xxx'),
	db.Field('ValorTotal', type='double', label=T(u'ValorTotal'),comment='xxx'),
	db.Field('Cantidad', type='double', label=T(u'Cantidad'),comment='xxx'),
	db.Field('ValorIva', type='double', label=T(u'ValorIva'),comment='xxx'),
	db.Field('FechaEntragaMaterial', type='date', label=T(u'FechaEntragaMaterial'),comment='xxx'),
	db.Field('Descricion', type='string', length=3000, label=T(u'Descricion'),comment='xxx')
	)
db.define_table('tbLineaPiloto',
	db.Field('IdPiloto', type='string', length=20, label=T(u'IdPiloto'),comment='xxx'),
	db.Field('IdProducto', type='double', label=T(u'IdProducto'),comment='xxx'),
	db.Field('cantidad', type='double', label=T(u'cantidad'),comment='xxx'),
	db.Field('ValorTotal', type='double', label=T(u'ValorTotal'),comment='xxx'),
	db.Field('ValorIva', type='double', label=T(u'ValorIva'),comment='xxx')
	)
db.define_table('tbLineaProducFacturaAnulada',
	db.Field('IdVenta', type='double', label=T(u'IdVenta'),comment='xxx'),
	db.Field('IdProducto', type='text', length=10, label=T(u'IdProducto'),comment='xxx'),
	db.Field('Motivo', type='text', length=1, label=T(u'Motivo'),comment='xxx'),
	db.Field('fecha', type='date', label=T(u'fecha'),comment='xxx'),
	db.Field('Descripcin', type='string', length=2000, label=T(u'Descripcin'),comment='xxx')
	)
db.define_table('tbLinea_Compra',
	db.Field('Consecutivo', type='double', label=T(u'Consecutivo'),comment='xxx'),
	db.Field('IdCompra', type='string', length=15, label=T(u'IdCompra'),comment='xxx'),
	db.Field('IdProducto', type='integer', label=T(u'IdProducto'),comment='xxx'),
	db.Field('IdProveedor', type='string', length=20, label=T(u'IdProveedor'),comment='xxx'),
	db.Field('Cantidad', type='double', label=T(u'Cantidad'),comment='xxx'),
	db.Field('ValorUnitario', type='double', label=T(u'ValorUnitario'),comment='xxx'),
	db.Field('ValorIva', type='double', label=T(u'ValorIva'),comment='xxx'),
	db.Field('IdCuenta', type='text', length=8, label=T(u'IdCuenta'),comment='xxx')
	)
db.define_table('tbLinea_Cotizaciones',
	db.Field('IdCotizacion', type='text', length=10, label=T(u'IdCotizacion'),comment='xxx'),
	db.Field('IdProducto', type='double', label=T(u'IdProducto'),comment='xxx'),
	db.Field('Cantidad', type='double', label=T(u'Cantidad'),comment='xxx'),
	db.Field('ValorTotal', type='double', label=T(u'ValorTotal'),comment='xxx'),
	db.Field('ValorIva', type='double', label=T(u'ValorIva'),comment='xxx')
	)
db.define_table('tbLinea_Produccion',
	db.Field('IdProduccion', type='text', length=5, label=T(u'IdProduccion'),comment='xxx'),
	db.Field('Paso', type='double', label=T(u'Paso'),comment='xxx'),
	db.Field('Descripcion', type='string', length=2000, label=T(u'Descripcion'),comment='xxx'),
	db.Field('Fecha', type='text', length=10, label=T(u'Fecha'),comment='xxx'),
	db.Field('Modificado_Paso', type='text', length=1, label=T(u'Modificado_Paso'),comment='xxx'),
	db.Field('IdEmpleado', type='string', length=15, label=T(u'IdEmpleado'),comment='xxx')
	)
db.define_table('tbLinea_Remision_Almacen',
	db.Field('IdRemision', type='double', label=T(u'IdRemision'),comment='xxx'),
	db.Field('IdUbicacionOrigina', type='text', length=2, label=T(u'IdUbicacionOrigina'),comment='xxx'),
	db.Field('IdProducto', type='double', label=T(u'IdProducto'),comment='xxx'),
	db.Field('Cantidad', type='double', label=T(u'Cantidad'),comment='xxx'),
	db.Field('ValorUnitario', type='double', label=T(u'ValorUnitario'),comment='xxx')
	)
db.define_table('tbLinea_Venta',
	db.Field('IdVenta', type='integer', label=T(u'IdVenta'),comment='xxx'),
	db.Field('IdProducto', type='integer', label=T(u'IdProducto'),comment='xxx'),
	db.Field('IdUbicacion', type='text', length=2, label=T(u'IdUbicacion'),comment='xxx'),
	db.Field('Cantidad', type='double', label=T(u'Cantidad'),comment='xxx'),
	db.Field('ValorTotalProducto', type='double', label=T(u'ValorTotalProducto'),comment='xxx'),
	db.Field('ValorIva', type='double', label=T(u'ValorIva'),comment='xxx'),
	db.Field('PorcentajeDescuento', type='double', label=T(u'PorcentajeDescuento'),comment='xxx')
	)
db.define_table('tbLineraPagoVales_Prestmos',
	db.Field('IdVales_Prestmos', type='text', length=10, label=T(u'IdVales_Prestmos'),comment='xxx'),
	db.Field('IdCuota', type='text', length=3, label=T(u'IdCuota'),comment='xxx'),
	db.Field('Valor', type='double', label=T(u'Valor'),comment='xxx'),
	db.Field('Fecha', type='date', label=T(u'Fecha'),comment='xxx'),
	db.Field('Observacion', type='string', length=2000, label=T(u'Observacion'),comment='xxx'),
	db.Field('IdEmpleado', type='string', length=15, label=T(u'IdEmpleado'),comment='xxx'),
	db.Field('IdUbicacion', type='text', length=2, label=T(u'IdUbicacion'),comment='xxx')
	)
db.define_table('tbLlamadasClientes',
	db.Field('IdLlamada', type='double', label=T(u'IdLlamada'),comment='xxx'),
	db.Field('IdEmpleado', type='string', length=15, label=T(u'IdEmpleado'),comment='xxx'),
	db.Field('NitEmpresa', type='string', length=20, label=T(u'NitEmpresa'),comment='xxx'),
	db.Field('FechaLlamada', type='date', label=T(u'FechaLlamada'),comment='xxx'),
	db.Field('FechaProximaLlamada', type='date', label=T(u'FechaProximaLlamada'),comment='xxx'),
	db.Field('DatosObservaciones', type='string', length=8000, label=T(u'DatosObservaciones'),comment='xxx'),
	db.Field('Cola', type='text', length=1, label=T(u'Cola'),comment='xxx')
	)
db.define_table('tbObjetos',
	db.Field('idObjeto', type='text', length=3, label=T(u'idObjeto'),comment='xxx'),
	db.Field('Formulario', type='string', length=50, label=T(u'Formulario'),comment='xxx'),
	db.Field('Descripcion', type='string', length=8000, label=T(u'Descripcion'),comment='xxx')
	)
db.define_table('tbOrdenePedidosTrabajo',
	db.Field('IdOrdenPedidoTrabajo', type='text', length=10, label=T(u'IdOrdenPedidoTrabajo'),comment='xxx'),
	db.Field('NitEmpresa', type='string', length=20, label=T(u'NitEmpresa'),comment='xxx'),
	db.Field('ValotTotal', type='double', label=T(u'ValotTotal'),comment='xxx'),
	db.Field('Valoriva', type='double', label=T(u'Valoriva'),comment='xxx'),
	db.Field('Fecha', type='date', label=T(u'Fecha'),comment='xxx'),
	db.Field('FechaEntraga', type='text', length=10, label=T(u'FechaEntraga'),comment='xxx'),
	db.Field('IdEmpleado', type='string', length=15, label=T(u'IdEmpleado'),comment='xxx'),
	db.Field('IdUbicacion', type='text', length=2, label=T(u'IdUbicacion'),comment='xxx'),
	db.Field('Descripcion', type='string', length=8000, label=T(u'Descripcion'),comment='xxx'),
	db.Field('Observaciones', type='string', length=8000, label=T(u'Observaciones'),comment='xxx')
	)
db.define_table('tbPagosEmpleados',
	db.Field('IdPago', type='string', length=15, label=T(u'IdPago'),comment='xxx'),
	db.Field('IdEmpleado', type='string', length=15, label=T(u'IdEmpleado'),comment='xxx'),
	db.Field('Fecha_Pago', type='date', label=T(u'Fecha_Pago'),comment='xxx'),
	db.Field('Valor_Pago', type='double', label=T(u'Valor_Pago'),comment='xxx'),
	db.Field('IdPeriodo', type='text', length=8, label=T(u'IdPeriodo'),comment='xxx'),
	db.Field('Observacion', type='string', length=8000, label=T(u'Observacion'),comment='xxx')
	)
db.define_table('tbPeriodoPagos',
	db.Field('IdPeriodo', type='text', length=8, label=T(u'IdPeriodo'),comment='xxx'),
	db.Field('FechaInicio', type='date', label=T(u'FechaInicio'),comment='xxx'),
	db.Field('FechaFin', type='date', label=T(u'FechaFin'),comment='xxx'),
	db.Field('Descripcion', type='string', length=3000, label=T(u'Descripcion'),comment='xxx')
	)
db.define_table('tbPermisosEmpleados',
	db.Field('NumPermiso', type='text', length=8, label=T(u'NumPermiso'),comment='xxx'),
	db.Field('IdPermiso', type='text', length=2, label=T(u'IdPermiso'),comment='xxx'),
	db.Field('IdEmpleado', type='string', length=15, label=T(u'IdEmpleado'),comment='xxx'),
	db.Field('FechaInicio', type='date', label=T(u'FechaInicio'),comment='xxx'),
	db.Field('FechaFinal', type='date', label=T(u'FechaFinal'),comment='xxx'),
	db.Field('Observaciones', type='string', length=8000, label=T(u'Observaciones'),comment='xxx')
	)
db.define_table('tbPermisosSoftware',
	db.Field('IdObjeto', type='text', length=3, label=T(u'IdObjeto'),comment='xxx'),
	db.Field('IdUsuarios', type='string', length=15, label=T(u'IdUsuarios'),comment='xxx')
	)
db.define_table('tbProduccion',
	db.Field('idProduccion', type='text', length=5, label=T(u'idProduccion'),comment='xxx'),
	db.Field('Nombre', type='string', length=100, label=T(u'Nombre'),comment='xxx'),
	db.Field('Comentario', type='string', length=1000, label=T(u'Comentario'),comment='xxx')
	)
db.define_table('tbProductos',
	db.Field('IdProducto', type='integer', label=T(u'IdProducto'),comment='xxx'),
	db.Field('CodBarra', type='string', length=30, label=T(u'CodBarra'),comment='xxx'),
	db.Field('Nombre', type='string', length=50, label=T(u'Nombre'),comment='xxx'),
	db.Field('PrecioCompra', type='double', label=T(u'PrecioCompra'),comment='xxx'),
	db.Field('PrecioUnitVenta', type='double', label=T(u'PrecioUnitVenta'),comment='xxx'),
	db.Field('PorcentajeIva', type='double', label=T(u'PorcentajeIva'),comment='xxx'),
	db.Field('IdCategoria', type='text', length=6, label=T(u'IdCategoria'),comment='xxx'),
	db.Field('Observacion', type='string', length=1000, label=T(u'Observacion'),comment='xxx'),
	db.Field('ProdPiloto', type='text', length=1, label=T(u'ProdPiloto'),comment='xxx'),
	db.Field('IvaIncluidoPrecio', type='text', length=1, label=T(u'IvaIncluidoPrecio'),comment='xxx'),
	db.Field('IdEmpleado', type='string', length=15, label=T(u'IdEmpleado'),comment='xxx'),
	db.Field('Fecha_Modificacion', type='date', label=T(u'Fecha_Modificacion'),comment='xxx')
	)
db.define_table('tbProductosPilotos',
	db.Field('IdPiloto', type='string', length=20, label=T(u'IdPiloto'),comment='xxx'),
	db.Field('Descripcion', type='string', length=8000, label=T(u'Descripcion'),comment='xxx'),
	db.Field('NitEmpresa', type='string', length=20, label=T(u'NitEmpresa'),comment='xxx'),
	db.Field('CostoProduccion', type='double', label=T(u'CostoProduccion'),comment='xxx'),
	db.Field('Cantidad', type='text', length=3, label=T(u'Cantidad'),comment='xxx'),
	db.Field('FechaSalidaProd', type='date', label=T(u'FechaSalidaProd'),comment='xxx'),
	db.Field('EstadoSalidaProducto', type='string', length=1000, label=T(u'EstadoSalidaProducto'),comment='xxx'),
	db.Field('FechaEntradaProd', type='date', label=T(u'FechaEntradaProd'),comment='xxx'),
	db.Field('EstadoEntradaProducto', type='string', length=1000, label=T(u'EstadoEntradaProducto'),comment='xxx'),
	db.Field('FechaPactadaEntrega', type='date', label=T(u'FechaPactadaEntrega'),comment='xxx')
	)
db.define_table('tbProveedores',
	db.Field('IdProveedor', type='string', length=20, label=T(u'IdProveedor'),comment='xxx'),
	db.Field('Empresa', type='string', length=30, label=T(u'Empresa'),comment='xxx'),
	db.Field('Direccion', type='string', length=40, label=T(u'Direccion'),comment='xxx'),
	db.Field('Telefono', type='string', length=20, label=T(u'Telefono'),comment='xxx'),
	db.Field('IdContacto', type='string', length=15, label=T(u'IdContacto'),comment='xxx'),
	db.Field('NombreContacto', type='string', length=40, label=T(u'NombreContacto'),comment='xxx'),
	db.Field('Mail', type='string', length=40, label=T(u'Mail'),comment='xxx'),
	db.Field('observacion', type='string', length=2000, label=T(u'observacion'),comment='xxx')
	)
db.define_table('tbRemisionesProdAlmacen',
	db.Field('IdRemision', type='integer', label=T(u'IdRemision'),comment='xxx'),
	db.Field('IdProducto', type='integer', label=T(u'IdProducto'),comment='xxx'),
	db.Field('IdUbicacionOrigen', type='text', length=2, label=T(u'IdUbicacionOrigen'),comment='xxx'),
	db.Field('Festringemision', type='date', label=T(u'Festringemision'),comment='xxx'),
	db.Field('IdUbicacionDestino', type='text', length=2, label=T(u'IdUbicacionDestino'),comment='xxx'),
	db.Field('idEmpleado', type='string', length=15, label=T(u'idEmpleado'),comment='xxx'),
	db.Field('Cantidad', type='double', label=T(u'Cantidad'),comment='xxx')
	)
db.define_table('tbRemisiones_Almacenes',
	db.Field('IdRemision', type='integer', label=T(u'IdRemision'),comment='xxx'),
	db.Field('IdUbicacionOrigina', type='text', length=2, label=T(u'IdUbicacionOrigina'),comment='xxx'),
	db.Field('IdUbicacionOrigen', type='text', length=2, label=T(u'IdUbicacionOrigen'),comment='xxx'),
	db.Field('IdUbicacionDestino', type='text', length=2, label=T(u'IdUbicacionDestino'),comment='xxx'),
	db.Field('IdEmpleado', type='string', length=15, label=T(u'IdEmpleado'),comment='xxx'),
	db.Field('Fecha', type='date', label=T(u'Fecha'),comment='xxx'),
	db.Field('Anulada', type='text', length=1, label=T(u'Anulada'),comment='xxx')
	)
db.define_table('tbTipoUbicacion',
	db.Field('IdTipoUbicacion', type='text', length=1, label=T(u'IdTipoUbicacion'),comment='xxx'),
	db.Field('NombreTipo', type='string', length=20, label=T(u'NombreTipo'),comment='xxx'),
	db.Field('Descripcion', type='string', length=3000, label=T(u'Descripcion'),comment='xxx')
	)
db.define_table('tbTurnoEmpleado',
	db.Field('IdTurno', type='text', length=2, label=T(u'IdTurno'),comment='xxx'),
	db.Field('Nombre', type='string', length=40, label=T(u'Nombre'),comment='xxx'),
	db.Field('Hora_Entrada', type='time', label=T(u'Hora_Entrada'),comment='xxx'),
	db.Field('Hora_Salida', type='time', label=T(u'Hora_Salida'),comment='xxx'),
	db.Field('Hora_Entrada_Sabados', type='time', label=T(u'Hora_Entrada_Sabados'),comment='xxx'),
	db.Field('Hora_Salida_Sabados', type='time', label=T(u'Hora_Salida_Sabados'),comment='xxx'),
	db.Field('Hora_Entrada_Domingos', type='time', label=T(u'Hora_Entrada_Domingos'),comment='xxx'),
	db.Field('Hora_Salida_Domingos', type='time', label=T(u'Hora_Salida_Domingos'),comment='xxx'),
	db.Field('Domingo', type='text', length=1, label=T(u'Domingo'),comment='xxx'),
	db.Field('Lunes', type='text', length=1, label=T(u'Lunes'),comment='xxx'),
	db.Field('Mates', type='text', length=1, label=T(u'Mates'),comment='xxx'),
	db.Field('Miercoles', type='text', length=1, label=T(u'Miercoles'),comment='xxx'),
	db.Field('Jueves', type='text', length=1, label=T(u'Jueves'),comment='xxx'),
	db.Field('Viernes', type='text', length=1, label=T(u'Viernes'),comment='xxx'),
	db.Field('Sabado', type='text', length=1, label=T(u'Sabado'),comment='xxx')
	)
db.define_table('tbUbicacionBodegaAlmacen',
	db.Field('IdUbicacion', type='text', length=2, label=T(u'IdUbicacion'),comment='xxx'),
	db.Field('NombreUbicacion', type='string', length=40, label=T(u'NombreUbicacion'),comment='xxx'),
	db.Field('IdTipoUbicacion', type='text', length=1, label=T(u'IdTipoUbicacion'),comment='xxx'),
	db.Field('Direccion', type='string', length=40, label=T(u'Direccion'),comment='xxx'),
	db.Field('Telefono', type='string', length=20, label=T(u'Telefono'),comment='xxx')
	)
db.define_table('tbUbicacionProductosBA',
	db.Field('IdProducto', type='double', label=T(u'IdProducto'),comment='xxx'),
	db.Field('IdUbicacion', type='text', length=2, label=T(u'IdUbicacion'),comment='xxx'),
	db.Field('CantidadDisponible', type='double', label=T(u'CantidadDisponible'),comment='xxx'),
	db.Field('CantidadRequerida', type='double', label=T(u'CantidadRequerida'),comment='xxx')
	)
db.define_table('tbUsuarios',
	db.Field('IdUsuarios', type='string', length=15, label=T(u'IdUsuarios'),comment='xxx'),
	db.Field('Usuario', type='string', length=20, label=T(u'Usuario'),comment='xxx'),
	db.Field('Clave', type='string', length=15, label=T(u'Clave'),comment='xxx'),
	db.Field('Tipo', type='string', length=15, label=T(u'Tipo'),comment='xxx')
	)
db.define_table('tbVales_Prestamos_Remisiones',
	db.Field('IdVales_Prestamos', type='text', length=10, label=T(u'IdVales_Prestamos'),comment='xxx'),
	db.Field('NitEmpresa', type='string', length=20, label=T(u'NitEmpresa'),comment='xxx'),
	db.Field('IdEmpleado', type='string', length=15, label=T(u'IdEmpleado'),comment='xxx'),
	db.Field('IdUbicacion', type='text', length=2, label=T(u'IdUbicacion'),comment='xxx'),
	db.Field('PrecioTotal', type='double', label=T(u'PrecioTotal'),comment='xxx'),
	db.Field('TotalIva', type='double', label=T(u'TotalIva'),comment='xxx'),
	db.Field('FechaPrestamo', type='date', label=T(u'FechaPrestamo'),comment='xxx'),
	db.Field('Estado', type='text', length=1, label=T(u'Estado'),comment='xxx'),
	db.Field('Tipo', type='text', length=1, label=T(u'Tipo'),comment='xxx'),
	db.Field('Observacion', type='string', length=8000, label=T(u'Observacion'),comment='xxx')
	)
db.define_table('tbVentas',
	db.Field('IdVenta', type='integer', label=T(u'IdVenta'),comment='xxx'),
	db.Field('IdUbicacion', type='text', length=2, label=T(u'IdUbicacion'),comment='xxx'),
    db.Field('NumFactura', type='text', label=T(u'Numero Factura'),comment='Contiene el Número de la factura'),
	db.Field('NitEmpresa', type='string', length=20, label=T(u'NitEmpresa'),comment='xxx'),
	db.Field('TotalVenta', type='double', label=T(u'TotalVenta'),comment='xxx'),
	db.Field('TotalIva', type='double', label=T(u'TotalIva'),comment='xxx'),
	db.Field('IdEmpleado', type='string', length=15, label=T(u'IdEmpleado'),comment='xxx'),
	db.Field('Fecha', type='date', label=T(u'Fecha'),comment='xxx'),
	db.Field('Hora', type='time', label=T(u'Hora'),comment='xxx'),
	db.Field('NoCuotas', type='text', length=2, label=T(u'NoCuotas'),comment='xxx'),
	db.Field('FechaVence', type='date', label=T(u'FechaVence'),comment='xxx'),
	db.Field('Pagada', type='text', length=1, label=T(u'Pagada'),comment='xxx'),
	db.Field('Anulada', type='text', length=1, label=T(u'Anulada'),comment='xxx'),
	db.Field('Observacion', type='string', length=1000, label=T(u'Observacion'),comment='xxx')
	)
db.define_table('tbconfigura',
	db.Field('idempresa', type='text', label=T(u'Codígo Empresa'),comment='xxx'),
	db.Field('IdUbicacion', type='text', label=T(u'Ubicacion'),comment='xxx'),#, db.tbUbicacionBodegaAlmacen)
    #db.tbconfigura.IdUbicacion.requires = IS_IN_DB(db, 'tbUbicacionBodegaAlmacen.id', '%(IdUbicacion)s',zero=T('Elige uno'))
    db.Field('RepProd', type='text', label=T(u'Repetir Producto Factura'),comment='Repetir produto en la factura de compra')
	)
