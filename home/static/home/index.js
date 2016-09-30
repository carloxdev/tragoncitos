$(document).ready ( function () {
	st = new Sitio()
})

function Sitio() {

	this.calendario = $('#calendario');

	this.modal = $('#win_calendar');

	this.Init();
}
Sitio.prototype.Init = function () {
	

	this.calendario.fullCalendar({
    	weekends: false,
    	locale: 'es',
    	// dayClick: this.Click_Dia,
    	eventClick: this.Click_Evento,
    	viewRender: this.Change_Month,
	});	

	this.modal.on('shown.bs.modal',this, this.Dibuja_Calendario)	
}
Sitio.prototype.Dibuja_Calendario = function(e) {
    e.data.calendario.fullCalendar('today');

    var newEvent = new Object();
	newEvent.title = "Menu";
	newEvent.start = new Date();
	newEvent.allDay = true;    

	e.data.calendario.fullCalendar( 'renderEvent', newEvent );

}
Sitio.prototype.Click_Dia = function(date, event, view) {

	anio = date.format("YYYY");
	mes = date.format("M");
	dia = date.format("D");

	var url = '/reservaciones/nueva/'+anio+'/'+mes+'/'+dia+'/'

	window.location.href = url
}
Sitio.prototype.Click_Evento = function(calEvent, jsEvent, view) {

	anio = calEvent.start.format("YYYY")
	mes = calEvent.start.format("M")
	dia = calEvent.start.format("D")

	var url = '/comanda/reservaciones/nueva/'+anio+'/'+mes+'/'+dia+'/'
	window.location.href = url
}
Sitio.prototype.Change_Month = function(view, element) {
	alert("hola")	
}