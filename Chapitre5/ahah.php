<?php
public function create(string $username, string $email, string $password): bool 
{
    // Préparation de la requête pour éviter une injection SQL avec prepare()
    $query = "INSERT INTO users (username, email, password) VALUES (:username, :email, :password)";
    $stmt = $this->db->prepare($query);

    // Exécution de la requête avec execute() et avec la sécurisation contre les injections SQL
    return $stmt->execute([
        'username' => $username,
        'email'    => $email,
        'password' => password_hash($password, PASSWORD_BCRYPT) // Petit hashage du mot de passe
    ]);
}