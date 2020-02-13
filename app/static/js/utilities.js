// set html header attributes
function setupHeader() {
	console.log("setup header function called");
	var navWidth = $("nav").css("width");
	navWidth = parseInt(navWidth);
	console.log("navbar width: ",navWidth);
	$(".endo-dd").css("right",navWidth/8);
};

// size upload buttons ("upload.html")
function sizeButtons(){
	
	div_width = $("#button-row").css("width");
	div_width = parseInt(div_width);
	console.log("jQuery div width: ",div_width);
	btn_width = Math.round(div_width/6);
	
	$(".btn-endo").css("width",btn_width);
	console.log("button width",btn_width);
	whiteSpace = div_width-2*btn_width;
	btn_spacer = Math.round(whiteSpace/12);
	console.log("spacer width",btn_spacer);
	$(".btn-left").css("right",btn_spacer);
	$(".btn-right").css("left",btn_spacer);
};

// setup reader characterization upload page
function setupUpload() {
	console.log("setup function called")
	$(".dropdown-toggle").dropdown();
	console.log("call setup header");
	setupHeader(); // set the navbar geometry
	
	console.log("attach event to buttons") // add events to buttons
	$('#buttonid').click(function(){
	$('#fileid').click();
	console.log("you clicked the fake button")
	});
	$('#submitButton').click(function(){;
		$('#formid').submit();
	});
	
	console.log("set button geometry");
	sizeButtons();
	console.log("endsetup");
};

// set "plotter.html" attributes
function setupPlotter() {
	console.log("setting up plotter");
	setupHeader();
	$(".dropdown-toggle").dropdown();
};

function plotData() {
	var parseTime = d3.timeParse("%Y-%m-%d %H:%M:%S");
	var formatTime = d3.timeFormat("%M");
	// dt = parseTime(sub)
	// console.log("dt: ",dt)
	
	var td = [] ;
	for(var i=0; i<data.length; i++) {
		row = data[i]
		dt = new Date(row[1]);
		ins = {date: dt, price:row[0]}
		td.push(ins)
		v = formatTime(dt)
	//	console.log("dt value: ",v);
	};
	// console.log('td: ',td)
	
	xScale = d3.scaleTime()
				.domain([
					d3.min(td, function(d) { return d.date;}),
					d3.max(td, function(d) {return d.date;})
				])
				.range([padding*2,w-padding]);
				
	yScale = d3.scaleLinear()
				.domain([
					d3.min(td, function(d) {return d.price;}),
					d3.max(td, function(d) {return d.price;})
				])
				.range([h-padding,padding]);
	
	// define the axis
	xAxis = d3.axisBottom()
					.scale(xScale)
					.ticks(9)
					.tickFormat(formatTime)
					
	// define y axis
	yAxis = d3.axisLeft()
		.scale(yScale)
		.ticks(10)
		
	var xmin = d3.min(td, function(d) {return d.date;});
	console.log("xmin: ",xmin)
	
	// add data to plot
	svg1.selectAll("circle")
		.data(td)
		.enter()
		.append("circle")
		.attr("cx",function(d){
			return xScale(d.date);
		})
		.attr("cy",function(d){
			return yScale(d.price);
		})
		.attr("r",2)
		
	// create X axis
	svg1.append("g")
		.attr("class","axis")
		.attr("transform","translate(0," + (h - padding) + ")")
		.call(xAxis)
		
	// create Y axis
	svg1.append("g")
		.attr("class","axis")
		.attr("id","yAxis")
		.attr("transform","translate(" + 2*padding + ",0)")
		.call(yAxis)

	// children = $("#yAxis") .children().(".g")
	// var children = $("#yAxis").find("g")[0]
	var formatYaxis = $("#yAxis").find("g").find("text").each(function() {
		val = $(this).text();
		if(!val.includes("$")){
			val = "$"+val;
			
		};
		// val = "$"+val;
		console.log("text value: ",val);
		test = val.includes("$");
		/*
		console.log("TEEEEESTTTTT",test);
		if(test) {
			console.log("TEST PASSED");
		} else {
			console.log("TEST FAILED");
		};
		*/
		$(this).text(val);
		$(this).css("color","green");
			});
		};
