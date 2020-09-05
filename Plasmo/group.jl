using JLD2
# # explicitly
# jldopen("example.jld2", "w") do file
#     mygroup = JLD2.Group(file, "mygroup")
#     mygroup["mystuff"] = 42
# end

# # implicitly
# jldopen("example.jld2", "w") do file
#     file["mygroup/mystuff"] = 43
# end

# file = jldopen("example.jld2", "r")

jldopen("example.jld2", "r") do file
    @assert file["mygroup"]["mystuff"] == 42
end
