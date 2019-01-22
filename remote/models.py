# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Category(models.Model):

    id = models.CharField(db_column="Id_Categoria_DI", max_length=5, primary_key=True)
    description = models.CharField(db_column="Desc_Categoria_DI", max_length=50)
    # identification_di = models.CharField(db_column='Identificacion_DI', max_length=2)
    classification = models.CharField(db_column="Clasificacion_DI", max_length=1)
    # years_di = models.SmallIntegerField(db_column='Anos_DI')

    class Meta:
        managed = False
        db_table = "RH_Categorias_Docente_Invest"
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return " ".join([self.id, self.desc_category_di]).strip()


@python_2_unicode_compatible
class Position(models.Model):

    id = models.CharField(db_column="Id_Cargo", max_length=5, primary_key=True)
    name = models.CharField(db_column="Desc_Cargo", max_length=120)

    category_name = models.CharField(db_column="Desc_Categoria", max_length=25)
    subcategory_name = models.CharField(db_column="Desc_Subcategoria", max_length=50)

    basic_wage = models.DecimalField(db_column="Salario_Basico", max_digits=10, decimal_places=4)
    seniority = models.DecimalField(db_column="Antiguedad", max_digits=10, decimal_places=4)

    # rgrupo = models.CharField(db_column='RGrupo', max_length=5)
    # ngrupo = models.CharField(db_column='NGrupo', max_length=3)
    # id_categoria = models.CharField(db_column='Id_Categoria', max_length=5)
    # id_subcategoria = models.CharField(db_column='Id_Subcategoria', max_length=5)
    # resolucion = models.CharField(db_column='Resolucion', max_length=20)
    # clasificacion = models.CharField(db_column='Clasificacion', max_length=1)
    # porciento_simultaneidad = models.DecimalField(db_column='Porciento_Simultaneidad', max_digits=19, decimal_places=6)
    # funcionario = models.BooleanField(db_column='Funcionario')
    # ejecutivo = models.BooleanField(db_column='Ejecutivo')
    # apoyo = models.BooleanField(db_column='Apoyo')
    # reportflag = models.BooleanField(db_column='ReportFlag')
    # coeficiente_multioficio = models.DecimalField(db_column='Coeficiente_Multioficio', max_digits=19, decimal_places=6)
    # coeficente_empresa_empleadora = models.DecimalField(db_column='Coeficente_Empresa_Empleadora', max_digits=8, decimal_places=2)
    # mscodgrupo = models.CharField(db_column='MSCodGrupo', max_length=3)
    # plus = models.DecimalField(db_column='Plus', max_digits=10, decimal_places=4)
    # salario_cargo = models.DecimalField(db_column='Salario_Cargo', max_digits=10, decimal_places=4)
    # estimulo = models.DecimalField(db_column='Estimulo', max_digits=10, decimal_places=4)
    # otros = models.DecimalField(db_column='Otros', max_digits=10, decimal_places=4)
    # ieterritorial = models.DecimalField(db_column='IETerritorial', max_digits=5, decimal_places=2)
    # etsector = models.DecimalField(db_column='ETSector', max_digits=5, decimal_places=2)
    # otrasretribuciones = models.DecimalField(db_column='OtrasRetribuciones', max_digits=8, decimal_places=2)
    # horarioirregular = models.DecimalField(db_column='HorarioIrregular', max_digits=10, decimal_places=4)
    # otras_cla = models.DecimalField(db_column='Otras_CLA', max_digits=10, decimal_places=4)
    # id_clasif_p2 = models.CharField(db_column='Id_Clasif_P2', max_length=3)

    class Meta:
        managed = False
        db_table = "RH_Cargos"
        verbose_name = "Position"
        verbose_name_plural = "Positions"

    def __str__(self):
        return " ".join([self.id, self.name]).strip()


@python_2_unicode_compatible
class Specialty(models.Model):

    id = models.CharField(db_column="Id_Especialidad", max_length=3, primary_key=True)
    name = models.CharField(db_column="Desc_Especialidad", max_length=25)

    class Meta:
        managed = False
        db_table = "RH_Profesiones_General"
        verbose_name = "Specialty"
        verbose_name_plural = "Specialties"

    def __str__(self):
        return " ".join([self.id, self.name]).strip()


@python_2_unicode_compatible
class Profession(models.Model):
    specialty = models.ForeignKey("Specialty", db_column="Id_Especialidad", blank=True, null=True)
    id = models.CharField(db_column="Id_Profesion", max_length=5, primary_key=True)
    name = models.CharField(db_column="Desc_Profesion", max_length=80)
    # id_especialidad = models.CharField(db_column='Id_Especialidad', max_length=3)

    class Meta:
        managed = False
        db_table = "RH_Profesiones"
        verbose_name = "Profession"
        verbose_name_plural = "Professions"

    def __str__(self):
        return " ".join([self.id, self.name]).strip()


@python_2_unicode_compatible
class Department(models.Model):

    id = models.CharField(db_column="Id_Ccosto", primary_key=True, max_length=15)
    name = models.TextField(db_column="Desc_Ccosto")

    class Meta:
        managed = False
        db_table = "Centro_Costo"
        verbose_name = "Department"
        verbose_name_plural = "Departments"

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Employee(models.Model):

    id = models.CharField(db_column="Id_Empleado", primary_key=True, max_length=15)
    fid = models.CharField(db_column="Id_Expediente", max_length=15)
    cid = models.CharField(db_column="No_CI", max_length=15)

    name = models.TextField(db_column="Nombre")
    surname1 = models.TextField(db_column="Apellido_1")
    surname2 = models.TextField(db_column="Apellido_2")

    active = models.NullBooleanField(db_column="Alta")
    inactive = models.NullBooleanField(db_column="Baja")

    phone = models.TextField(db_column="Telefono_Particular")
    department = models.ForeignKey("Department", db_column="Id_CCosto", blank=True, null=True)

    category = models.ForeignKey("Category", db_column="Id_Categoria_DI", blank=True, null=True)
    position = models.ForeignKey("Position", db_column="Id_Cargo", blank=True, null=True)
    profession = models.ForeignKey("Profession", db_column="Id_Profesion", max_length=5, blank=True, null=True)

    address = models.TextField(db_column="Direccion")
    city = models.TextField(db_column="Ciudad")
    region = models.TextField(db_column="Region")
    postal_code = models.TextField(db_column="Codigo_Postal")
    country = models.TextField(db_column="Pais")

    date_hired = models.DateField(db_column="Fecha_Contratacion")

    # id_profesion = models.CharField(db_column='Id_Profesion', max_length=5)
    # id_category = models.CharField(db_column='Id_Categoria', max_length=5)
    # id_ccosto = models.CharField(db_column='Id_CCosto', max_length=10)
    # exttelef = models.CharField(db_column='Exttelef', max_length=15)
    # fecha_nacimiento = models.DateTimeField(db_column='Fecha_Nacimiento')
    # nota = models.TextField(db_column='Nota')
    # tipo_pago = models.SmallIntegerField(db_column='Tipo_Pago')
    # id_tipo_contrato = models.CharField(db_column='Id_Tipo_Contrato', max_length=3)
    # regimen_salarial = models.SmallIntegerField(db_column='Regimen_Salarial')
    # tarifa_horaria_con_reporte = models.NullBooleanField(db_column='Tarifa_Horaria_con_Reporte')
    # calendario = models.CharField(db_column='Calendario', max_length=3)
    # descontarsabado = models.NullBooleanField(db_column='DescontarSabado')
    # id_cargo = models.CharField(db_column='Id_Cargo', max_length=5)
    # ngrupo = models.SmallIntegerField(db_column='NGrupo')
    # fecha_cargo = models.DateTimeField(db_column='Fecha_Cargo')
    # asignacion_por_cargo = models.NullBooleanField(db_column='Asignacion_por_Cargo')
    # nivel = models.SmallIntegerField(db_column='Nivel')
    # id_direccion = models.CharField(db_column='Id_Direccion', max_length=15)
    # plaza = models.BigIntegerField(db_column='Plaza')
    # id_causaalta = models.CharField(db_column='Id_CausaAlta', max_length=5)
    # id_fundamentacionalta = models.CharField(db_column='Id_FundamentacionAlta', max_length=5)
    # id_causabaja = models.CharField(db_column='Id_CausaBaja', max_length=5)
    # fecha_baja = models.DateTimeField(db_column='Fecha_Baja')
    # dias_descontar_alta = models.SmallIntegerField(db_column='Dias_Descontar_Alta')
    # dias_descontar_mov = models.SmallIntegerField(db_column='Dias_Descontar_Mov')
    # dias_descontar_baja = models.SmallIntegerField(db_column='Dias_Descontar_Baja')
    # saya = models.CharField(db_column='Saya', max_length=5)
    # pantalon = models.CharField(db_column='Pantalon', max_length=5)
    # camisa = models.CharField(db_column='Camisa', max_length=5)
    # zapato = models.CharField(db_column='Zapato', max_length=5)
    # sexo = models.CharField(db_column='Sexo', max_length=1)
    # color_piel = models.SmallIntegerField(db_column='Color_Piel')
    # color_pelo = models.SmallIntegerField(db_column='Color_Pelo')
    # estatura = models.DecimalField(db_column='Estatura', max_digits=7, decimal_places=2)
    # nombre_madre = models.TextField(db_column='Nombre_Madre')
    # nombre_padre = models.TextField(db_column='Nombre_Padre')
    # id_provincia = models.CharField(db_column='Id_Provincia', max_length=5)
    # id_municipio = models.CharField(db_column='Id_Municipio', max_length=5)
    # id_nivel_escolaridad = models.CharField(db_column='Id_Nivel_Escolaridad', max_length=3)
    # fecha_terminacion_contrato = models.DateTimeField(db_column='Fecha_Terminacion_Contrato')
    # docente = models.NullBooleanField(db_column='Docente')
    # investigador = models.NullBooleanField(db_column='Investigador')
    ## id_categoria_di = models.CharField(db_column='Id_Categoria_DI', max_length=5)# anoiniciodocencia = models.IntegerField(db_column='AnoInicioDocencia')
    # anointerruptodocencia = models.IntegerField(db_column='AnoInterruptoDocencia')
    # numero_radicacion_plaza = models.CharField(db_column='Numero_Radicacion_Plaza', max_length=50)
    # id_ubicacion_defensa = models.CharField(db_column='Id_Ubicacion_Defensa', max_length=5)
    # especificacion_defensa = models.TextField(db_column='Especificacion_Defensa')
    # imprescindible = models.NullBooleanField(db_column='Imprescindible')
    # fechamilitar = models.DateTimeField(db_column='FechaMilitar')
    # oc = models.NullBooleanField(db_column='OC')
    # militancia = models.SmallIntegerField(db_column='Militancia')
    # requisitoidiomatico = models.NullBooleanField(db_column='RequisitoIdiomatico')
    # requisitotecnico = models.NullBooleanField(db_column='RequisitoTecnico')
    # id_obra = models.CharField(db_column='Id_Obra', max_length=10)
    # tipo_vacuna = models.SmallIntegerField(db_column='Tipo_Vacuna')
    # fecha_vacuna = models.DateTimeField(db_column='Fecha_Vacuna')
    # nota_vacuna = models.TextField(db_column='Nota_Vacuna')
    # nivel_cp = models.SmallIntegerField(db_column='Nivel_CP')
    # id_direccion_cp = models.CharField(db_column='Id_Direccion_CP', max_length=15)
    # id_cargo_cp = models.CharField(db_column='Id_Cargo_CP', max_length=5)
    # id_categoria_cp = models.CharField(db_column='Id_Categoria_CP', max_length=5)
    # ngrupo_cp = models.SmallIntegerField(db_column='NGrupo_CP')
    # fecha_cargo_cp = models.DateTimeField(db_column='Fecha_Cargo_CP')
    # asignacion_por_cargo_cp = models.NullBooleanField(db_column='Asignacion_por_Cargo_CP')
    # id_grpevaluativo = models.CharField(db_column='Id_GrpEvaluativo', max_length=7)
    # id_grpsendrec = models.CharField(db_column='Id_GrpSendRec', max_length=7)
    # cuadroreserva = models.SmallIntegerField(db_column='CuadroReserva')
    # clasifcuadros = models.SmallIntegerField(db_column='ClasifCuadros')
    # situacionreserva = models.SmallIntegerField(db_column='SituacionReserva')
    # nivel_reserva = models.SmallIntegerField(db_column='Nivel_Reserva')
    # id_direccion_reserva = models.CharField(db_column='Id_Direccion_Reserva', max_length=15)
    # id_cargo_reserva = models.CharField(db_column='Id_Cargo_Reserva', max_length=5)
    # anosservicio = models.SmallIntegerField(db_column='AnosServicio')
    # antiguedaddispensa = models.SmallIntegerField(db_column='AntiguedadDispensa')
    # situacion = models.SmallIntegerField(db_column='Situacion')
    # id_actividad = models.CharField(db_column='Id_Actividad', max_length=3)
    # albergado = models.NullBooleanField(db_column='Albergado')
    # cubiculo = models.CharField(db_column='Cubiculo', max_length=5)
    # modulouniforme = models.CharField(db_column='ModuloUniforme', max_length=50)
    # fechasector = models.DateTimeField(db_column='FechaSector')
    # fechadireccion = models.DateTimeField(db_column='FechaDireccion')
    # mision_civil = models.NullBooleanField(db_column='Mision_Civil')
    # mision_militar = models.NullBooleanField(db_column='Mision_Militar')
    # ayuda_tecnica = models.NullBooleanField(db_column='Ayuda_Tecnica')
    # microbrigada = models.NullBooleanField(db_column='Microbrigada')
    # doble_expediente = models.NullBooleanField(db_column='Doble_Expediente')
    # disposicioncargo = models.NullBooleanField(db_column='DisposicionCargo')
    # prestacion_servicio = models.NullBooleanField(db_column='Prestacion_Servicio')
    # fecha_prestacion_servicio = models.DateTimeField(db_column='Fecha_Prestacion_Servicio')
    # mision = models.SmallIntegerField(db_column='Mision')
    # foto = models.BinaryField(db_column='Foto', blank=True, null=True)
    # id_user = models.CharField(db_column='Id_User', max_length=15)
    # fecha_op = models.DateTimeField(db_column='Fecha_Op')
    # id_subcategoria = models.CharField(db_column='Id_Subcategoria', max_length=5)
    # id_categoria_it = models.CharField(db_column='Id_Categoria_IT', max_length=5)
    # id_jornada = models.CharField(db_column='Id_Jornada', max_length=5)
    # id_tarjeta_reloj = models.CharField(db_column='Id_Tarjeta_Reloj', max_length=15)
    # tarjeta_reloj_on = models.NullBooleanField(db_column='Tarjeta_Reloj_On')
    # designacion = models.NullBooleanField(db_column='Designacion')
    # dias_dec_ley_91 = models.DecimalField(db_column='Dias_Dec_Ley_91', max_digits=10, decimal_places=4)
    # dias_dec_ley_91_saldo = models.DecimalField(db_column='Dias_Dec_Ley_91_Saldo', max_digits=10, decimal_places=4)
    # horario_regular = models.NullBooleanField(db_column='Horario_Regular')
    # id_grado_cientifico = models.CharField(db_column='Id_Grado_Cientifico', max_length=5)
    # fecha_categoria_docente = models.DateTimeField(db_column='Fecha_Categoria_Docente')

    class Meta:
        managed = False
        db_table = "Empleados_Gral"
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

    def __str__(self):
        return " ".join([self.name, self.surname1, self.surname2]).strip()

