using JLD2

# # data = jldopen("Plasmo\\13_piplines.jld2","r")
# data = jldopen("Plasmo\\13_pipelines.jld2","r")

# junction = read(data, "junction_data")
# compressor = read(data, "compressor_data")
# pipeline = read(data, "pipeline_data")

# println(junction)
# println(compressor)
# println(pipeline)

jldfile = jldopen("Plasmo\\13_pipelines.jld2","r")
junction_data = jldfile["junction_data"]
pipeline_data = jldfile["pipeline_data"]
compressor_data = jldfile["compressor_data"]
close(jldfile)

#setup topology dictionaries
junction_map_in = Dict()    #pipeline into each junction
junction_map_out = Dict()   #pipelines out of each junction
pipe_map = Dict()           #junction connected to each pipeline
compressor_map = Dict()
jmap = Dict()

# #create junction models.
# junctions = []
# for (i,j_data) in junction_data
#     jmodel = create_junction_model(j_data,nt)
#     junction_map_in[jmodel] = []
#     junction_map_out[jmodel] = []
#     jmap[i] = jmodel
#     push!(junctions,jmodel)
# end

print(junctions)