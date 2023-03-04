package main

import (
    "fmt"
    "net/http"
    "os"
)

func main() {
    // Define a health check endpoint that returns HTTP 200 OK
    http.HandleFunc("/healthz", func(w http.ResponseWriter, r *http.Request) {
        w.WriteHeader(http.StatusOK)
        fmt.Fprintf(w, "OK")
    })

    // Define a readiness check endpoint that returns HTTP 200 OK once a dependent service is available
    http.HandleFunc("/readyz", func(w http.ResponseWriter, r *http.Request) {
        // Check if a dependent service is available (e.g., a database connection)
        if isReady() {
            w.WriteHeader(http.StatusOK)
            fmt.Fprintf(w, "OK")
        } else {
            w.WriteHeader(http.StatusServiceUnavailable)
            fmt.Fprintf(w, "Not ready")
        }
    })

    // Start the HTTP server
    port := os.Getenv("PORT")
    if port == "" {
        port = "8080"
    }
    fmt.Printf("Listening on port %s...\n", port)
    err := http.ListenAndServe(fmt.Sprintf(":%s", port), nil)
    if err != nil {
        panic(err)
    }
}

// A function that checks if a dependent service is available
func isReady() bool {
    // Check if the database connection is established
    // Replace this with your own readiness check logic
    return true
}

