package main.java.com.firstTry.demo;

import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class AdminController {
    @PostMapping("/api/mute")
    
    public String muteUser() {
        // Implement mute user functionality here
        return "User muted";
    }

    @PostMapping("/api/unmute")
    public String unmuteUser() {
        // Implement unmute user functionality here
        return "User unmuted";
    }

    @PostMapping("/api/kick")
    public String kickUser() {
        // Implement kick user functionality here
        return "User kicked";
    }

    @PostMapping("/api/ban")
    public String banUser() {
        // Implement ban user functionality here
        return "User banned";
    }

    @PostMapping("/api/unban")
    public String unbanUser() {
        // Implement unban user functionality here
        return "User unbanned";
    }

    @PostMapping("/api/editRoles")
    public String editUserRoles() {
        // Implement edit user roles functionality here
        return "User roles edited";
    }

}
