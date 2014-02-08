#http://shoesrb.com/walkthrough.html

#we want... rotation, vertical offset & number of steps back
def process_code(text)
	data = {}
	bounds = text.split("\n")[0].split(" ")[-1].split("..")
	start = bounds[0].to_i
	finish = bounds[1].to_i
	num_steps = finish - start + 1
	vertical_bound = self.height - 200 - 20
	data["num_steps"] = num_steps
	data["step_rotation"] = -(360 / (num_steps - 1))
	data["vertical_step"] = vertical_bound / (num_steps - 1)
	data
end

 
Shoes.app(width: 300, height: 600) do
	stack(margin: 10) do
		para "Enter loop code"
		@code_window = edit_box
		@code_window.style(width: 280)
		@button = button "See Loop loop"
		@button.click {
			#do the stuff....
			data = process_code(@code_window.text)
			translate 20, 200
			data["num_steps"].times do |i|
				arrow(0, data["vertical_step"]*i, 20)
				rotate data["step_rotation"]
			end
		}
	end
end