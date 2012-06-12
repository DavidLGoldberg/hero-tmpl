from hero_tmpl import create_app

if __name__ == "__main__":
    #TODO: make configurable string
    print "Starting Server."
    app = create_app()

    import os
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

print "App Imported"
