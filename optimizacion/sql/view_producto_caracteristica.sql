CREATE or REPLACE VIEW producto_caracteristica as
SELECT *, 
(SELECT oc.valor from optimizacion_caracteristica oc WHERE producto_id = op.id and oc.nombre = 'm3/d') as M3d,
(SELECT oc.valor from optimizacion_caracteristica oc WHERE producto_id = op.id and oc.nombre ='TPD') as TPD,
(SELECT oc.valor from optimizacion_caracteristica oc WHERE producto_id = op.id and oc.nombre ='Dens, TON/M3') as Dens,
(SELECT oc.valor from optimizacion_caracteristica oc WHERE producto_id = op.id and oc.nombre ='Azufre, PPM') as Azufre,
(SELECT oc.valor from optimizacion_caracteristica oc WHERE producto_id = op.id and oc.nombre ='RON') as RON,
(SELECT oc.valor from optimizacion_caracteristica oc WHERE producto_id = op.id and oc.nombre ='RBN') as RBN,
(SELECT oc.valor from optimizacion_caracteristica oc WHERE producto_id = op.id and oc.nombre ='RVP, atm') as RVP,
(SELECT oc.valor from optimizacion_caracteristica oc WHERE producto_id = op.id and oc.nombre ='IMPVR') as IMPVR,
(SELECT oc.valor from optimizacion_caracteristica oc WHERE producto_id = op.id and oc.nombre ='Naft. % Vol') as Naft,
(SELECT oc.valor from optimizacion_caracteristica oc WHERE producto_id = op.id and oc.nombre ='Arom. %Vol') as Arom
FROM optimizacion_producto op 