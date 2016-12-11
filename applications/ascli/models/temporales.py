# -*- coding: utf-8 -*-
db.define_table('tbtmp_linea_venta',
	db.Field('IdVenta', type='integer', label=T(u'IdVenta'),comment='xxx'),
	db.Field('IdProducto', type='integer', label=T(u'IdProducto'),comment='xxx'),
	db.Field('NombreProducto', type='text', label=T(u'NombreProducto'),comment='xxx'),
	db.Field('IdUbicacion', type='text', length=2, label=T(u'IdUbicacion'),comment='xxx'),
	db.Field('Cantidad', type='integer', label=T(u'Cantidad'),comment='xxx'),
	db.Field('ValorTotalProducto', type='double', label=T(u'ValorTotalProducto'),comment='xxx'),
	db.Field('ValorIva', type='double', label=T(u'ValorIva'),comment='xxx'),
	db.Field('PorcentajeDescuento', type='double', label=T(u'PorcentajeDescuento'),comment='xxx')
	)

db.define_table('tbtmp_ventas',
	db.Field('IdVenta', type='integer', label=T(u'IdVenta'),comment='xxx'),
	db.Field('IdUbicacion', type='text', length=2, label=T(u'IdUbicacion'),comment='xxx'),
	db.Field('NitEmpresa', type='string', length=20, label=T(u'NitEmpresa'),comment='xxx'),
	db.Field('TotalVenta', type='double', label=T(u'TotalVenta'),comment='xxx'),
	db.Field('TotalIva', type='double', label=T(u'TotalIva'),comment='xxx'),
	db.Field('IdEmpleado', type='string', length=15, label=T(u'IdEmpleado'),comment='xxx'),
	db.Field('NoCuotas', type='text', length=2, label=T(u'NoCuotas'),comment='xxx'),
	db.Field('FechaVence', type='date', label=T(u'FechaVence'),comment='xxx'),
	db.Field('Observacion', type='string', length=1000, label=T(u'Observacion'),comment='xxx')
	)
