watch("hero_tmpl/less/.*\.less$") do |match|
    system("lessc less/style.less public/css/style.css")
    puts "updating styles."
end

# watch("app.py") do |match|
#     system("foreman stop")
#     system("foreman start")
#     puts "restarting foreman."
# end
