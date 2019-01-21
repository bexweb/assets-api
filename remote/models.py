# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Category(models.Model):
    id = models.CharField(db_column='Id_Categoria_DI', max_length=5, primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='Desc_Categoria_DI', max_length=50)  # Field name made lowercase.
    #identification_di = models.CharField(db_column='Identificacion_DI', max_length=2)  # Field name made lowercase.
    classification = models.CharField(db_column='Clasificacion_DI', max_length=1)  # Field name made lowercase.
    #years_di = models.SmallIntegerField(db_column='Anos_DI')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RH_Categorias_Docente_Invest'
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return " ".join([self.id, self.desc_category_di]).strip()


@python_2_unicode_compatible
class Charge(models.Model):
    id = models.CharField(db_column='Id_Cargo', max_length=5, primary_key=True)  # Field name made lowercase.
    nameCharge = models.CharField(db_column='Desc_Cargo', max_length=120)  # Field name made lowercase.
    nameCategory = models.CharField(db_column='Desc_Categoria', max_length=25)  # Field name made lowercase.
    nameSubcategory = models.CharField(db_column='Desc_Subcategoria', max_length=50)  # Field name made lowercase.
    basicSalary = models.DecimalField(db_column='Salario_Basico', max_digits=10, decimal_places=4)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    antiquity = models.DecimalField(db_column='Antiguedad', max_digits=10, decimal_places=4)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float

    # rgrupo = models.CharField(db_column='RGrupo', max_length=5)  # Field name made lowercase.
    # ngrupo = models.CharField(db_column='NGrupo', max_length=3)  # Field name made lowercase.
    # id_categoria = models.CharField(db_column='Id_Categoria', max_length=5)  # Field name made lowercase.
    # id_subcategoria = models.CharField(db_column='Id_Subcategoria', max_length=5)  # Field name made lowercase.
    # resolucion = models.CharField(db_column='Resolucion', max_length=20)  # Field name made lowercase.
    # clasificacion = models.CharField(db_column='Clasificacion', max_length=1)  # Field name made lowercase.
    # porciento_simultaneidad = models.DecimalField(db_column='Porciento_Simultaneidad', max_digits=19, decimal_places=6)  # Field name made lowercase.
    # funcionario = models.BooleanField(db_column='Funcionario')  # Field name made lowercase.
    # ejecutivo = models.BooleanField(db_column='Ejecutivo')  # Field name made lowercase.
    # apoyo = models.BooleanField(db_column='Apoyo')  # Field name made lowercase.
    # reportflag = models.BooleanField(db_column='ReportFlag')  # Field name made lowercase.
    # coeficiente_multioficio = models.DecimalField(db_column='Coeficiente_Multioficio', max_digits=19, decimal_places=6)  # Field name made lowercase.
    # coeficente_empresa_empleadora = models.DecimalField(db_column='Coeficente_Empresa_Empleadora', max_digits=8, decimal_places=2)  # Field name made lowercase.
    # mscodgrupo = models.CharField(db_column='MSCodGrupo', max_length=3)  # Field name made lowercase.
    # plus = models.DecimalField(db_column='Plus', max_digits=10, decimal_places=4)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    # salario_cargo = models.DecimalField(db_column='Salario_Cargo', max_digits=10, decimal_places=4)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    # estimulo = models.DecimalField(db_column='Estimulo', max_digits=10, decimal_places=4)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    # otros = models.DecimalField(db_column='Otros', max_digits=10, decimal_places=4)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    # ieterritorial = models.DecimalField(db_column='IETerritorial', max_digits=5, decimal_places=2)  # Field name made lowercase.
    # etsector = models.DecimalField(db_column='ETSector', max_digits=5, decimal_places=2)  # Field name made lowercase.
    # otrasretribuciones = models.DecimalField(db_column='OtrasRetribuciones', max_digits=8, decimal_places=2)  # Field name made lowercase.
    # horarioirregular = models.DecimalField(db_column='HorarioIrregular', max_digits=10, decimal_places=4)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    # otras_cla = models.DecimalField(db_column='Otras_CLA', max_digits=10, decimal_places=4)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    # id_clasif_p2 = models.CharField(db_column='Id_Clasif_P2', max_length=3)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RH_Cargos'
        verbose_name = "Charge"
        verbose_name_plural = "Charges"

    def __str__(self):
        return " ".join([self.id, self.name]).strip()


@python_2_unicode_compatible
class Specialty(models.Model):
    id = models.CharField(db_column='Id_Especialidad', max_length=3, primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Desc_Especialidad', max_length=25)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RH_Profesiones_General'

    def __str__(self):
        return " ".join([self.id, self.name]).strip()


@python_2_unicode_compatible
class Profession(models.Model):
    specialty = models.ForeignKey("Specialty", db_column="Id_Especialidad", blank=True, null=True)
    id = models.CharField(db_column='Id_Profesion', max_length=5, primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Desc_Profesion', max_length=80)  # Field name made lowercase.
    #id_especialidad = models.CharField(db_column='Id_Especialidad', max_length=3)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RH_Profesiones'
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
    charge = models.ForeignKey("Charge", db_column="Id_Cargo", blank=True, null=True)
    profession = models.ForeignKey("Profession", db_column='Id_Profesion', max_length=5, blank=True, null=True)
    address = models.TextField(db_column='Direccion')  # Field name made lowercase.
    city = models.TextField(db_column='Ciudad')  # Field name made lowercase.
    land = models.TextField(db_column='Region')  # Field name made lowercase.
    postal_code = models.TextField(db_column='Codigo_Postal')  # Field name made lowercase.
    country = models.TextField(db_column='Pais')  # Field name made lowercase.
    date_contract = models.DateTimeField(db_column='Fecha_Contratacion')  # Field name made lowercase.

    # id_profesion = models.CharField(db_column='Id_Profesion', max_length=5)  # Field name made lowercase.
    # id_category = models.CharField(db_column='Id_Categoria', max_length=5)  # Field name made lowercase.
    # id_ccosto = models.CharField(db_column='Id_CCosto', max_length=10)  # Field name made lowercase.
    # exttelef = models.CharField(db_column='Exttelef', max_length=15)  # Field name made lowercase.
    # fecha_nacimiento = models.DateTimeField(db_column='Fecha_Nacimiento')  # Field name made lowercase.
    # nota = models.TextField(db_column='Nota')  # Field name made lowercase.
    # tipo_pago = models.SmallIntegerField(db_column='Tipo_Pago')  # Field name made lowercase.
    # id_tipo_contrato = models.CharField(db_column='Id_Tipo_Contrato', max_length=3)  # Field name made lowercase.
    # regimen_salarial = models.SmallIntegerField(db_column='Regimen_Salarial')  # Field name made lowercase.
    # tarifa_horaria_con_reporte = models.NullBooleanField(db_column='Tarifa_Horaria_con_Reporte')  # Field name made lowercase.
    # calendario = models.CharField(db_column='Calendario', max_length=3)  # Field name made lowercase.
    # descontarsabado = models.NullBooleanField(db_column='DescontarSabado')  # Field name made lowercase.
    #id_charge = models.CharField(db_column='Id_Cargo', max_length=5)  # Field name made lowercase.
    # ngrupo = models.SmallIntegerField(db_column='NGrupo')  # Field name made lowercase.
    # fecha_cargo = models.DateTimeField(db_column='Fecha_Cargo')  # Field name made lowercase.
    # asignacion_por_cargo = models.NullBooleanField(db_column='Asignacion_por_Cargo')  # Field name made lowercase.
    # nivel = models.SmallIntegerField(db_column='Nivel')  # Field name made lowercase.
    # id_direccion = models.CharField(db_column='Id_Direccion', max_length=15)  # Field name made lowercase.
    # plaza = models.BigIntegerField(db_column='Plaza')  # Field name made lowercase.
    # id_causaalta = models.CharField(db_column='Id_CausaAlta', max_length=5)  # Field name made lowercase.
    # id_fundamentacionalta = models.CharField(db_column='Id_FundamentacionAlta', max_length=5)  # Field name made lowercase.
    # id_causabaja = models.CharField(db_column='Id_CausaBaja', max_length=5)  # Field name made lowercase.
    # fecha_baja = models.DateTimeField(db_column='Fecha_Baja')  # Field name made lowercase.
    # dias_descontar_alta = models.SmallIntegerField(db_column='Dias_Descontar_Alta')  # Field name made lowercase.
    # dias_descontar_mov = models.SmallIntegerField(db_column='Dias_Descontar_Mov')  # Field name made lowercase.
    # dias_descontar_baja = models.SmallIntegerField(db_column='Dias_Descontar_Baja')  # Field name made lowercase.
    # saya = models.CharField(db_column='Saya', max_length=5)  # Field name made lowercase.
    # pantalon = models.CharField(db_column='Pantalon', max_length=5)  # Field name made lowercase.
    # camisa = models.CharField(db_column='Camisa', max_length=5)  # Field name made lowercase.
    # zapato = models.CharField(db_column='Zapato', max_length=5)  # Field name made lowercase.
    # sexo = models.CharField(db_column='Sexo', max_length=1)  # Field name made lowercase.
    # color_piel = models.SmallIntegerField(db_column='Color_Piel')  # Field name made lowercase.
    # color_pelo = models.SmallIntegerField(db_column='Color_Pelo')  # Field name made lowercase.
    # estatura = models.DecimalField(db_column='Estatura', max_digits=7, decimal_places=2)  # Field name made lowercase.
    # nombre_madre = models.TextField(db_column='Nombre_Madre')  # Field name made lowercase.
    # nombre_padre = models.TextField(db_column='Nombre_Padre')  # Field name made lowercase.
    # id_provincia = models.CharField(db_column='Id_Provincia', max_length=5)  # Field name made lowercase.
    # id_municipio = models.CharField(db_column='Id_Municipio', max_length=5)  # Field name made lowercase.
    # id_nivel_escolaridad = models.CharField(db_column='Id_Nivel_Escolaridad', max_length=3)  # Field name made lowercase.
    # fecha_terminacion_contrato = models.DateTimeField(db_column='Fecha_Terminacion_Contrato')  # Field name made lowercase.
    # docente = models.NullBooleanField(db_column='Docente')  # Field name made lowercase.
    # investigador = models.NullBooleanField(db_column='Investigador')  # Field name made lowercase.
    ## id_categoria_di = models.CharField(db_column='Id_Categoria_DI', max_length=5)  # Field name made lowercase.# anoiniciodocencia = models.IntegerField(db_column='AnoInicioDocencia')  # Field name made lowercase.
    # anointerruptodocencia = models.IntegerField(db_column='AnoInterruptoDocencia')  # Field name made lowercase.
    # numero_radicacion_plaza = models.CharField(db_column='Numero_Radicacion_Plaza', max_length=50)  # Field name made lowercase.
    # id_ubicacion_defensa = models.CharField(db_column='Id_Ubicacion_Defensa', max_length=5)  # Field name made lowercase.
    # especificacion_defensa = models.TextField(db_column='Especificacion_Defensa')  # Field name made lowercase.
    # imprescindible = models.NullBooleanField(db_column='Imprescindible')  # Field name made lowercase.
    # fechamilitar = models.DateTimeField(db_column='FechaMilitar')  # Field name made lowercase.
    # oc = models.NullBooleanField(db_column='OC')  # Field name made lowercase.
    # militancia = models.SmallIntegerField(db_column='Militancia')  # Field name made lowercase.
    # requisitoidiomatico = models.NullBooleanField(db_column='RequisitoIdiomatico')  # Field name made lowercase.
    # requisitotecnico = models.NullBooleanField(db_column='RequisitoTecnico')  # Field name made lowercase.
    # id_obra = models.CharField(db_column='Id_Obra', max_length=10)  # Field name made lowercase.
    # tipo_vacuna = models.SmallIntegerField(db_column='Tipo_Vacuna')  # Field name made lowercase.
    # fecha_vacuna = models.DateTimeField(db_column='Fecha_Vacuna')  # Field name made lowercase.
    # nota_vacuna = models.TextField(db_column='Nota_Vacuna')  # Field name made lowercase.
    # nivel_cp = models.SmallIntegerField(db_column='Nivel_CP')  # Field name made lowercase.
    # id_direccion_cp = models.CharField(db_column='Id_Direccion_CP', max_length=15)  # Field name made lowercase.
    # id_cargo_cp = models.CharField(db_column='Id_Cargo_CP', max_length=5)  # Field name made lowercase.
    # id_categoria_cp = models.CharField(db_column='Id_Categoria_CP', max_length=5)  # Field name made lowercase.
    # ngrupo_cp = models.SmallIntegerField(db_column='NGrupo_CP')  # Field name made lowercase.
    # fecha_cargo_cp = models.DateTimeField(db_column='Fecha_Cargo_CP')  # Field name made lowercase.
    # asignacion_por_cargo_cp = models.NullBooleanField(db_column='Asignacion_por_Cargo_CP')  # Field name made lowercase.
    # id_grpevaluativo = models.CharField(db_column='Id_GrpEvaluativo', max_length=7)  # Field name made lowercase.
    # id_grpsendrec = models.CharField(db_column='Id_GrpSendRec', max_length=7)  # Field name made lowercase.
    # cuadroreserva = models.SmallIntegerField(db_column='CuadroReserva')  # Field name made lowercase.
    # clasifcuadros = models.SmallIntegerField(db_column='ClasifCuadros')  # Field name made lowercase.
    # situacionreserva = models.SmallIntegerField(db_column='SituacionReserva')  # Field name made lowercase.
    # nivel_reserva = models.SmallIntegerField(db_column='Nivel_Reserva')  # Field name made lowercase.
    # id_direccion_reserva = models.CharField(db_column='Id_Direccion_Reserva', max_length=15)  # Field name made lowercase.
    # id_cargo_reserva = models.CharField(db_column='Id_Cargo_Reserva', max_length=5)  # Field name made lowercase.
    # anosservicio = models.SmallIntegerField(db_column='AnosServicio')  # Field name made lowercase.
    # antiguedaddispensa = models.SmallIntegerField(db_column='AntiguedadDispensa')  # Field name made lowercase.
    # situacion = models.SmallIntegerField(db_column='Situacion')  # Field name made lowercase.
    # id_actividad = models.CharField(db_column='Id_Actividad', max_length=3)  # Field name made lowercase.
    # albergado = models.NullBooleanField(db_column='Albergado')  # Field name made lowercase.
    # cubiculo = models.CharField(db_column='Cubiculo', max_length=5)  # Field name made lowercase.
    # modulouniforme = models.CharField(db_column='ModuloUniforme', max_length=50)  # Field name made lowercase.
    # fechasector = models.DateTimeField(db_column='FechaSector')  # Field name made lowercase.
    # fechadireccion = models.DateTimeField(db_column='FechaDireccion')  # Field name made lowercase.
    # mision_civil = models.NullBooleanField(db_column='Mision_Civil')  # Field name made lowercase.
    # mision_militar = models.NullBooleanField(db_column='Mision_Militar')  # Field name made lowercase.
    # ayuda_tecnica = models.NullBooleanField(db_column='Ayuda_Tecnica')  # Field name made lowercase.
    # microbrigada = models.NullBooleanField(db_column='Microbrigada')  # Field name made lowercase.
    # doble_expediente = models.NullBooleanField(db_column='Doble_Expediente')  # Field name made lowercase.
    # disposicioncargo = models.NullBooleanField(db_column='DisposicionCargo')  # Field name made lowercase.
    # prestacion_servicio = models.NullBooleanField(db_column='Prestacion_Servicio')  # Field name made lowercase.
    # fecha_prestacion_servicio = models.DateTimeField(db_column='Fecha_Prestacion_Servicio')  # Field name made lowercase.
    # mision = models.SmallIntegerField(db_column='Mision')  # Field name made lowercase.
    # foto = models.BinaryField(db_column='Foto', blank=True, null=True)  # Field name made lowercase.
    # id_user = models.CharField(db_column='Id_User', max_length=15)  # Field name made lowercase.
    # fecha_op = models.DateTimeField(db_column='Fecha_Op')  # Field name made lowercase.
    # id_subcategoria = models.CharField(db_column='Id_Subcategoria', max_length=5)  # Field name made lowercase.
    # id_categoria_it = models.CharField(db_column='Id_Categoria_IT', max_length=5)  # Field name made lowercase.
    # id_jornada = models.CharField(db_column='Id_Jornada', max_length=5)  # Field name made lowercase.
    # id_tarjeta_reloj = models.CharField(db_column='Id_Tarjeta_Reloj', max_length=15)  # Field name made lowercase.
    # tarjeta_reloj_on = models.NullBooleanField(db_column='Tarjeta_Reloj_On')  # Field name made lowercase.
    # designacion = models.NullBooleanField(db_column='Designacion')  # Field name made lowercase.
    # dias_dec_ley_91 = models.DecimalField(db_column='Dias_Dec_Ley_91', max_digits=10, decimal_places=4)  # Field name made lowercase.
    # dias_dec_ley_91_saldo = models.DecimalField(db_column='Dias_Dec_Ley_91_Saldo', max_digits=10, decimal_places=4)  # Field name made lowercase.
    # horario_regular = models.NullBooleanField(db_column='Horario_Regular')  # Field name made lowercase.
    # id_grado_cientifico = models.CharField(db_column='Id_Grado_Cientifico', max_length=5)  # Field name made lowercase.
    # fecha_categoria_docente = models.DateTimeField(db_column='Fecha_Categoria_Docente')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "Empleados_Gral"
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

    def __str__(self):
        return " ".join([self.name, self.surname1, self.surname2]).strip()

