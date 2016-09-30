$(document).ready ( function () {
	st = new Sitio()
})

function Sitio() {

	this.calendario = $('#calendario');

	this.modal = $('#win_calendar');

	this.Init();
}
Sitio.prototype.Init = function () {
	
	$("#list-platos-fuertes label input").change(this, this.Click_Check)

	this.calendario.fullCalendar({
    	weekends: false,
    	locale: 'es',
    	dayClick: this.Click_Dia,
	});	

	this.modal.on('shown.bs.modal',this, this.Dibuja_Calendario)	
}
Sitio.prototype.Click_Check = function(e) {

	valor = e.currentTarget.value

	// Deshabilitar componente
	check_opt = "#list-platos-fuertes-opt label input[value=XXX]".replace('XXX', valor)
	$check_opt = $(check_opt)

	// Desmarcar si esta Marcado
	if ($check_opt.is(':checked')) {
		$check_opt.prop("checked", false)
	}

	// Deshabilitar
	$check_opt.attr("disabled", true);

	// Habilitar los demas
	other_checks = "#list-platos-fuertes-opt label input[value!=XXX]".replace('XXX', valor)
	lista = $(other_checks)

	lista.each(function (indice, elemento) {
		$(elemento).removeAttr("disabled");
	});
}
Sitio.prototype.Dibuja_Calendario = function(e) {

    e.data.calendario.fullCalendar('today');

}
Sitio.prototype.Click_Dia = function(date, event, view) {

	anio = date.format("YYYY");
	mes = date.format("M");
	dia = date.format("D");

	var url = '/comanda/reservaciones/nueva/'+anio+'/'+mes+'/'+dia+'/'

	window.location.href = url
}